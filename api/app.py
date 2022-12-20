import os
from flask import Flask
from flask_jwt_extended import jwt_manager

# models import
from .models import db, ma, migrate, jwt
from flask_sqlalchemy import SQLAlchemy

# controllers import
from .controllers.user_controller import user_api as user_blueprint

from api.Config import Config


# from extensions import db

def create_app(env_name):
    api_url = '/api/v1/'
    app = Flask(__name__)
    app.config.from_object(Config)

    # app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql+psycopg2://ismaila:Iss141792@localhost/asset_management"
    # app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    # app.debug = False

    # db = SQLAlchemy(app)

    db.init_app(app)
    ma.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)

    app.register_blueprint(user_blueprint)

    @app.route('/', methods=['GET'])
    def index():
        return 'No access'

    return app
