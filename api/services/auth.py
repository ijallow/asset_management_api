from flask_jwt_extended import create_access_token, create_refresh_token, get_jwt_identity
from http import HTTPStatus
from passlib.hash import pbkdf2_sha256

# from ..models.UserModel import UserModel, UserSchema


# from api.models import UserModel


def hash_password(password):
    return pbkdf2_sha256.hash(password)


def check_password(password, hashed):
    return pbkdf2_sha256.verify(password, hashed)


def login_service(email, password):
    # user = UserModel.get_by_email(email=email)
    #
    # if not user or not check_password(password, user.password):
    #     return {'message': 'email or password is incorrect'}, HTTPStatus.UNAUTHORIZED
    #
    # access_token = create_access_token(identity=user.id)
    # refresh_token = create_refresh_token(identity=user.id)
    #
    # return {access_token, refresh_token}
    pass


def refresh_service():
    pass

def logout_service():
    pass
    # return {'message': 'success', 'access_token': access_token}