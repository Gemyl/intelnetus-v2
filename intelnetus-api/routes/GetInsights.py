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