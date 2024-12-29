from routes.metadata import get_metadata
from routes.insights import get_metadata_insights

def register_routes(app, db, is_production_env, scopus_api_key):

    @app.route('/get-metadata', methods=['GET'])
    def invoke_get_metadata():
        result = get_metadata(db, is_production_env, scopus_api_key)
        return result
    
    @app.route('/get-insights', methods=['GET'])
    def invoke_get_metadata_insights():
        result = get_metadata_insights(db, is_production_env)
        return result