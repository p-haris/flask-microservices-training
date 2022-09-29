import os
import datetime

_deployed_env_ = os.environ.get("FLASK_ENV", default=None)
print(f"Environment: [{_deployed_env_}]")

class Config(object):
    TESTING = False
    JWT_SECRET_KEY = 'aasddffdr3434234eeerw'
    JWT_ACCESS_TOKEN_EXPIRES = datetime.timedelta(minutes=30)
    JWT_REFRESH_TOKEN_EXPIRES = datetime.timedelta(days=1)
    PMS_ADMIN_EMAIL = 'saurav@gmail.com'
    PMS_ADMIN_PASSWORD = 'saurav'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    #If set to True , Flask-SQLAlchemy will track modifications of objects
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:postgres@localhost:5432/product-management-db'
    #The database URI that should be used for the connection.

class ProductionConfig(Config):
    DATABASE_URI = 'product-management-prod.db'

class DevelopmentConfig(Config):
    DATABASE_URI = 'user-management-dev.db'
    
    DEBUG = True
    #debug=true is for debugging during development. It creates debugging symbols used to provide metadata about the current executing code. debug=false is is for deployment to a production server.

class TestingConfig(Config):
    DATABASE_URI = 'user-management-test.db'
    TESTING = True


def load_configuration(app):
    print(_deployed_env_)
    if (_deployed_env_ == None):
        app.config.from_object(DevelopmentConfig)
    elif (_deployed_env_ == 'dev'):
        app.config.from_object(DevelopmentConfig)
    elif (_deployed_env_ == 'testing'):
        app.config.from_object(TestingConfig)
    elif (_deployed_env_ == 'production'):
        app.config.from_object(ProductionConfig)
    else:
        raise RuntimeError('Unknown environment setting provided.')        
