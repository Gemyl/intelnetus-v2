from db.connection import get_db_connection_uri
from models import db
from dotenv import load_dotenv
from flask_cors import CORS
from flask import Flask
from flask_migrate import Migrate
from routing import register_routes
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

# the line below should be in comments in DEVELOPMENT environment
# os.environ['PYB_CONFIG_FILE'] = "/app/.pybliometrics/config.ini"

environment = 'PRODUCTION'
is_production_env = True

if(("--dev" in sys.argv) | ("db" in sys.argv)):
    environment = 'DEVELOPMENT'
    is_production_env = False

if(is_production_env):
    host = os.environ.get('DB_HOST_PROD')
else:
    host = os.environ.get('DB_HOST_DEV')

print(f'Application running in {environment} environment.')

app = Flask(__name__)
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = get_db_connection_uri(is_production_env)

db.init_app(app)

with app.app_context():
    db.create_all()

migrate = Migrate(app, db)

register_routes(app, db, is_production_env, scopus_api_key)

if __name__ == '__main__':
    app.run(debug=True)