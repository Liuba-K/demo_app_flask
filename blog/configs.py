import os

SQLALCHEMY_DATABASE_URI = 'sqlite:///D:\\IT\\projects\\Flask\\sqlite.db'
    #os.environ.get('SQLALCHEMY_DATABASE_URL')
SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = 'abcdefg123456'
    #os.getenv('SECRET_KEY')

WTF_CSRF_ENABLED = True
FLASK_ADMIN_SWATCH = 'cosmo'

OPENAPI_URL_PREFIX = '/api/swagger'
OPENAPI_SWAGGER_UI_PATH = '/'
OPENAPI_SWAGGER_UI_VERSION = '3.22.0'
