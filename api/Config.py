import os
from os import environ

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    DEBUG = True,
    SQLALCHEMY_DATABASE_URI = environ.get('POSTGRES_DB_URL')
    SECRET_KEY = environ.get('SECRET_KEY')
    JWT_ERROR_MESSAGE_KEY = environ.get('JWT_ERROR_MESSAGE_KEY')
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class Development:
    """
  Development environment
  
  """
    DEBUG = True
    TESTING = False
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = environ.get('POSTGRES_DB_URL')
    # SQLALCHEMY_DATABASE_URI = "postgresql+psycopg2://ismaila:Iss141792@localhost/asset_management"
