from Endpoints.Queries.GetMetadata.Receiver import get_metadata_receiver
from models import db
from dotenv import load_dotenv
from flask_cors import CORS
from flask import Flask
import pymysql
import mysql
import os
import sys

load_dotenv()
port = os.environ.get('DB_PORT')
user = os.environ.get('DB_USER')
password = os.environ.get('DB_PASSWORD')
database = os.environ.get('DB_NAME')
scopus_api_key = os.environ.get('SCOPUS_API_KEY')

environment = 'PRODUCTION'
is_production_env = True
for arg in sys.argv:
    if(arg == '--dev'):
        environment = 'DEVELOPMENT'
        is_production_env = False
        break

if(is_production_env):
    host = os.environ.get('DB_HOST_PROD')
else:
    host = os.environ.get('DB_HOST_DEV')

print(f'Application running in {environment} environment.')

app = Flask(__name__)
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+pymysql://{user}:{password}@{host}:{port}/{database}'

db.init_app(app)
with app.app_context():
    db.create_all()

@app.route('/get-metadata', methods=['GET'])
def get_metadata():
    result = get_metadata_receiver(scopus_api_key, is_production_env, db)
    return result

if __name__ == '__main__':
    app.run(debug=True)