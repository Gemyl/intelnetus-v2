from db.connection import open_db_session, close_db_session
from lib.helpers import get_scopus_fields
from flask import request

def get_publications_number_per_country(db, is_production_env):
    try:
        keywords = request.args.get("keywords").split(',')
        booleans = request.args.get("operators").split(',')
        fields = request.args.get("fields").split(',')
        start_year = request.args.get("startYear")
        end_year = request.args.get("endYear")
        fields_abbreviations = get_scopus_fields(fields)

        basic_query = "SELECT organizations.country, count(organizations.country) FROM ((publications\
            INNER JOIN publications_organizations ON publications.id = publications_organizations.publication_id)\
            INNER JOIN organizations ON publications_organizations.organization_id = organizations.id) "
        
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
        
        criteria_query = criteria_query + ") "

        group_query = " GROUP BY organizations.country"
        order_query = " ORDER BY count(organizations.country) DESC"
        limit_query = " LIMIT 0,5;"

        query = basic_query + criteria_query + group_query + order_query + limit_query

        cursor, connection = open_db_session(is_production_env)
        cursor.execute(query)
        data = cursor.fetchall()

        if(len(data) > 0):
            result = {
                "successful": True,
                "hasResult": True,
                "data": data
            }
        
        else:
            result = {
                "successful": True,
                "hasResult": False,
                "data": data
            }

    except Exception as err:
        result = {
            "successful": False,
            "hasResult": False,
            "errorMessage": str(err)
        }

    close_db_session(cursor, connection)
    return result


def get_publications_number_per_field(db, is_production_env):
    try:
        keywords = request.args.get("keywords").split(',')
        booleans = request.args.get("operators").split(',')
        fields = request.args.get("fields").split(',')
        start_year = request.args.get("startYear")
        end_year = request.args.get("endYear")
        fields_abbreviations = get_scopus_fields(fields)

        basic_query = "SELECT fields FROM publications"

        criteria_query = ' WHERE ('
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
        
        criteria_query = criteria_query + ");"
        query = basic_query + criteria_query

        cursor, connection = open_db_session(is_production_env)
        cursor.execute(query)
        fields = cursor.fetchall()

        if(len(fields) > 0):
            data = {}
            all_fields = [field for fields_row in fields for field in fields_row[0].split(",")]
            for field in all_fields:
                if(field not in data.keys()):
                    data[field] = 0
                else:
                    data[field] = data[field] + 1

            data = sorted(data.items(), key=lambda x: x[1], reverse=True)
            data = dict(data[:5])

            result = {
                "successful": True,
                "hasResult": True,
                "data": data
            }
        
        else:
            result = {
                "successful": True,
                "hasResult": False,
                "data": {}
            }

    
    except Exception as err:
        result = {
            "successful": True,
            "hasResult": False,
            "errorMessage": str(err)
        }
    
    close_db_session(cursor, connection)
    return result


def get_publications_fields_citations_per_year(db, is_production_env):
    try:
        keywords = request.args.get("keywords").split(',')
        booleans = request.args.get("operators").split(',')
        fields = request.args.get("fields").split(',')
        start_year = request.args.get("startYear")
        end_year = request.args.get("endYear")
        fields_abbreviations = get_scopus_fields(fields)
    
        basic_query = "SELECT year, fields, citations_count FROM publications"
        criteria_query = ' WHERE ('
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
        
        criteria_query = criteria_query + ");"
        query = basic_query + criteria_query

        cursor, connection = open_db_session(is_production_env)
        cursor.execute(query)
        data_fetched = cursor.fetchall()

        if(len(data_fetched) > 0):
            fields_citations_per_year = {}
            fields_citations_total = {}

            for item in data_fetched:
                for field in item[1].split(","):
                    if(field not in fields_citations_per_year.keys()):
                        fields_citations_per_year[field] = {}
                        fields_citations_per_year[field][item[0]] = item[2]
                    elif(item[0] not in fields_citations_per_year[field].keys()):
                        fields_citations_per_year[field][item[0]] = item[2]
                    else:
                        fields_citations_per_year[field][item[0]] = item[2] + fields_citations_per_year[field][item[0]]

                    if(field not in fields_citations_total.keys()):
                        fields_citations_total[field] = item[2]
                    else: 
                        fields_citations_total[field] = item[2] + fields_citations_total[field]
            
            fields_citations_total = sorted(fields_citations_total.items(), key=lambda x: x[1], reverse=True)
            fields_citations_total = dict(fields_citations_total[:5])
            
            data = {}
            for field in fields_citations_per_year.keys():
                if(field in fields_citations_total.keys()):
                     data[field] = fields_citations_per_year[field]

            for year in range(int(start_year), int(end_year)+1):
                for field in data.keys():
                    if(str(year) not in data[field].keys()):
                        data[field][str(year)] = 0

            result = {
                "successful": True,
                "hasResult": True,
                "data": data
            }

        else:
            result = {
                "successful": True,
                "hasResult": False,
                "data": fields_citations_per_year
            }
                   
    except Exception as err:
        result = {
            "successful": False,
            "hasResult": False,
            "errorMessage": str(err)
        }

    close_db_session(cursor, connection)
    return result