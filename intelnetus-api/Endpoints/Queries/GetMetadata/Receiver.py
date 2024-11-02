from Handlers.Metadata.Handler import get_scopus_fields, process_metadata
from Services.Database.Service import get_db_connection_and_cursor
from flask import request, jsonify
import json

def get_metadata_receiver(scopus_api_key, is_production_env, db):

    try:
        keywords = request.args.get("keywords").split(',')
        booleans = request.args.get("operators").split(',')
        fields = request.args.get("fields").split(',')
        start_year = request.args.get("startYear")
        end_year = request.args.get("endYear")
        fields_abbreviations = get_scopus_fields(fields)
        page_size = request.args.get("pageSize")
        offset = request.args.get("offset")
        filter_values = json.loads(request.args.get("filterValue"))
        excluded_variants = json.loads(request.args.get("exclude"))

        cursor, connection = get_db_connection_and_cursor(is_production_env)
        process_metadata(keywords, start_year, end_year, fields, booleans, scopus_api_key, db, is_production_env)

        selection_query = f"SELECT publications.id, publications.doi, publications.title, publications.year, \
                            publications.citations_count, publications.keywords, publications.fields, authors.id,  \
                            authors.first_name, authors.last_name, authors.study_fields, authors.citations_count,  \
                            authors.h_index, organizations.id, organizations.name, organizations.primary_type,  \
                            organizations.secondary_type, organizations.city, organizations.country "

        
        join_query = "FROM ((((publications_authors  \
                        INNER JOIN publications ON publications_authors.publication_id = publications.id)  \
                        INNER JOIN authors ON publications_authors.author_id = authors.id)  \
                        INNER JOIN authors_organizations ON authors.id = authors_organizations.author_id)  \
                        INNER JOIN organizations ON authors_organizations.organization_id = organizations.id)"
        
        basic_query = selection_query + join_query

        criteria_query = 'WHERE ('
        for i in range(len(keywords)):
            if (i == 0):
                subquery = f'publications.keywords LIKE \'%{keywords[i].lower()}%\' \
                            OR publications.title LIKE \'%{keywords[i].lower()}%\' \
                            OR publications.abstract LIKE \'%{keywords[i].lower()}%\''
                criteria_query = criteria_query + subquery
            else:
                subquery = f'{booleans[i-1]} `keywords` LIKE \'%{keywords[i].lower()}%\' \
                            OR publications.title LIKE \'%{keywords[i].lower()}%\' \
                            OR publications.abstract LIKE \'%{keywords[i].lower()}%\''
                criteria_query = criteria_query + subquery

        criteria_query = criteria_query + ')  AND '
        criteria_query = criteria_query + f'publications.year >= {start_year} '
        criteria_query = criteria_query + f'AND publications.year <= {end_year} AND  ('

        for i in range(len(fields_abbreviations)):
            if (i == 0):
                subquery = f'publications.fields_abbreviations LIKE \'%{fields_abbreviations[i]}%\''
                criteria_query = criteria_query + subquery
            else: 
                subquery = f' OR publications.fields_abbreviations LIKE \'%{fields_abbreviations[i]}%\''
                criteria_query = criteria_query + subquery
        
        criteria_query = criteria_query + ')'

        excluded_variants_query = ''
        for i in range(len(excluded_variants)):
            excluded_variants_query += f'AND {excluded_variants[i]["type"]}.id != \'{excluded_variants[i]["id"]}\''

        filter_query = ''
        if len(filter_values) > 0:
            for filter_index in range(len(filter_values)):
                if(filter_index == 0):
                    subquery = f'{filter_values[filter_index]["entity"]}.{filter_values[filter_index]["field"]} LIKE \'%{filter_values[filter_index]["value"]}%\''
                else:
                    subquery = f'{subquery} AND {filter_values[filter_index]["entity"]}.{filter_values[filter_index]["field"]} LIKE \'%{filter_values[filter_index]["value"]}%\''

            filter_query = f'AND ({subquery})'

        pagination_query = f" LIMIT {page_size} OFFSET {offset}"
        metadata_query = f'{criteria_query} {excluded_variants_query} {filter_query} {pagination_query};'

        query = basic_query + metadata_query

        data = []
        publications_ids = []
        authors_ids = []
        organizations_ids = []
        cursor.execute(query)
        metadata = cursor.fetchall()

        for row in metadata:
            publications_ids.append(row[0])
            authors_ids.append(row[7])
            organizations_ids.append(row[13])
            data.append({
                "publicationId":row[0],
                "publicationDoi":row[1],
                "publicationTitle":row[2],
                "publicationYear":row[3],
                "publicationCitationsCount":row[4],
                "publicationKeywords":row[5],
                "publicationFields":row[6],
                "authorId":row[7],
                "authorFirstName":row[8],
                "authorLastName":row[9],
                "authorFieldsOfStudy":row[10],
                "authorCitationsCount":row[11],
                "authorhIndex":row[12],
                "organizationId":row[13],
                "organizationName":row[14],
                "organizationType1":row[15],
                "organizationType2":row[16],
                "organizationCity":row[17],
                "organizationCountry":row[18]
            })

        publications_variants = {
            "originals":[],
            "duplicates":[]
        }

        query = "SELECT * FROM publications_variants;"
        cursor.execute(query)
        fetched_data = cursor.fetchall()

        for pub_var in fetched_data:
            original_id = pub_var[0]
            duplicate_id = pub_var[1]

            if ((original_id in publications_ids) & (duplicate_id in publications_ids)):
                sub_query = f"SELECT publications.id, publications.title, \
                            publications.citations_count FROM publications \
                            WHERE id = '{original_id}';"
                cursor.execute(sub_query)
                variant_data = cursor.fetchall()[0]
                publications_variants["originals"].append({
                    "id":variant_data[0],
                    "title":variant_data[1],
                    "citationsCount":variant_data[2],
                    "selected": False
                })

                sub_query = f"SELECT publications.id, publications.title, \
                            publications.citations_count FROM publications \
                            WHERE ID = '{duplicate_id}';"
                cursor.execute(sub_query)
                variant_data = cursor.fetchall()[0]
                publications_variants["duplicates"].append({
                    "id":variant_data[0],
                    "title":variant_data[1],
                    "citationsCount":variant_data[2],
                    "selected": False
                })

        authors_variants = {
            "originals":[],
            "duplicates":[]
        }

        query = "SELECT * FROM authors_variants;"
        cursor.execute(query)
        fetched_data = cursor.fetchall()

        for auth_var in fetched_data:
            original_id = auth_var[0]
            duplicate_id = auth_var[1]

            if ((original_id in authors_ids) & (duplicate_id in authors_ids)):
                sub_query = f"SELECT authors.id, authors.first_name, \
                            authors.last_name, authors.h_index, \
                            authors.citations_count FROM authors \
                WHERE id = '{original_id}';"
                cursor.execute(sub_query)
                variant_data = cursor.fetchall()[0]
                authors_variants["originals"].append({
                    "id":variant_data[0],
                    "firstName":variant_data[1],
                    "lastName":variant_data[2],
                    "hIndex":variant_data[3],
                    "citationsCount":variant_data[4],
                    "selected": False
                })

                sub_query = f"SELECT authors.id, authors.first_name, \
                            authors.last_name, authors.h_index, \
                            authors.citations_count FROM authors \
                WHERE id = '{duplicate_id}';"
                cursor.execute(sub_query)
                variant_data = cursor.fetchall()[0]
                authors_variants["duplicates"].append({
                    "id":variant_data[0],
                    "firstName":variant_data[1],
                    "lastName":variant_data[2],
                    "hIndex":variant_data[3],
                    "citationsCount":variant_data[4],
                    "selected": False
                })

        organizations_variants = {
            "originals":[],
            "duplicates":[]
        }

        query = "SELECT * FROM organizations_variants;"
        cursor.execute(query)
        fetched_data = cursor.fetchall()

        for org_var in fetched_data:
            original_id = org_var[0]
            duplicate_id = org_var[1]

            if ((original_id in organizations_ids) & (duplicate_id in organizations_ids)):
                sub_query = f"SELECT organizations.id, organizations.name FROM organizations \
                WHERE id = '{original_id}';"
                cursor.execute(sub_query)
                variant_data = cursor.fetchall()[0]
                organizations_variants["originals"].append({
                    "id":variant_data[0],
                    "name":variant_data[1],
                    "selected": False
                })

                sub_query = f"SELECT organizations.id, organizations.name FROM organizations \
                WHERE id = '{duplicate_id}';"
                cursor.execute(sub_query)
                variant_data = cursor.fetchall()[0]
                organizations_variants["duplicates"].append({
                    "id":variant_data[0],
                    "name":variant_data[1],
                    "selected": False
                })

        variants = {
            "publicationsVariants":publications_variants,
            "authorsVariants":authors_variants,
            "organizationsVariants":organizations_variants
        }

        query = f"SELECT COUNT(DOI) {join_query} {criteria_query} {filter_query};"
        cursor.execute(query)
        total = cursor.fetchall()[0][0]

        if (len(data) > 0):
            result = {
                "successful": "true",
                "hasResult": "true",
                "data": data,
                "variants": variants,
                "total": total
            }

        else:
            result = {
                "successful": "true",
                "hasResult": "false",
                "data": data,
                "variants": variants,
                "total": total
            }
    
    except Exception as err:
        result = {
            "successful":"false",
            "hasResult":"false",
            "errorMessage": str(err),
            "data":[],
            "variants":[]
        }

    return jsonify(result)