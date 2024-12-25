from routes.GetMetadata import get_metadata

def register_routes(app, db, is_production_env, scopus_api_key):

    @app.route('/get-metadata', methods=['GET'])
    def invoke_get_metadata():
        result = get_metadata(db, is_production_env, scopus_api_key)
        return result