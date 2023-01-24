from flask import Flask
from flask_cors import CORS

# models import
from .models import db, ma, migrate, jwt

# controllers import
from .controllers.UserController import user_api as user_blueprint
from .controllers.AssetController import asset_api as asset_blueprint
from .controllers.CategoryController import category_api as category_blueprint
from .controllers.AuthController import login_api as login_blueprint, black_list

from api.Config import Config


def create_app(env_name):
    api_url = '/api/v1/'
    app = Flask(__name__)
    # cors = CORS(app, supports_credentials=True, resources={r"/api/*": {"origins": "*"}})
    CORS(app)
    # cors = CORS(app, supports_credentials=True, resources={r"/api/*": {"origins": "*"}})
    app.config.from_object(Config)


    # from .models import user, assets

    # app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql+psycopg2://ismaila:Iss141792@localhost/asset_management"
    # app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    # app.debug = False

    # db = SQLAlchemy(app)

    db.init_app(app)
    ma.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)

    @jwt.token_in_blocklist_loader
    def check_if_token_in_blacklist(jwt_header, jwt_payload: dict):
        jti = jwt_payload['jti']

        return jti in black_list

    app.register_blueprint(user_blueprint)
    app.register_blueprint(asset_blueprint)
    app.register_blueprint(category_blueprint)
    app.register_blueprint(login_blueprint)

    @app.route('/', methods=['GET'])
    def index():
        return 'No access'

    return app
