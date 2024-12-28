from routes.GetMetadata import get_metadata
from routes.GetInsights import get_publications_number_per_country

def register_routes(app, db, is_production_env, scopus_api_key):

    @app.route('/get-metadata', methods=['GET'])
    def invoke_get_metadata():
        result = get_metadata(db, is_production_env, scopus_api_key)
        return result
    
    @app.route('/get-insights/publications-number-per-country', methods=['GET'])
    def invoke_get_insights():
        result = get_publications_number_per_country(db, is_production_env)
        return result