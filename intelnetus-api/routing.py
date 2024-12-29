from routes.metadata import get_metadata
from routes.insights import get_publications_number_per_country, get_publications_number_per_field, get_publications_fields_citations_per_year

def register_routes(app, db, is_production_env, scopus_api_key):

    @app.route('/get-metadata', methods=['GET'])
    def invoke_get_metadata():
        result = get_metadata(db, is_production_env, scopus_api_key)
        return result
    
    @app.route('/get-insights/publications-number-per-country', methods=['GET'])
    def invoke_get_publications_number_per_country():
        result = get_publications_number_per_country(db, is_production_env)
        return result
    
    @app.route('/get-insights/publications-number-per-field', methods=['GET'])
    def invoke_get_publications_number_per_fields():
        result = get_publications_number_per_field(db, is_production_env)
        return result
    
    @app.route('/get-insights/publications-fields-citations-per-year', methods=['GET'])
    def invoke_get_publications_fields_citations_per_years():
        result = get_publications_fields_citations_per_year(db, is_production_env)
        return result