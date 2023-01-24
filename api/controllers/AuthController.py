from flask import Blueprint, request, jsonify
from flask_jwt_extended import (create_access_token,
                                get_jwt_identity,
                                jwt_required,
                                create_refresh_token,
                                get_jwt)
from http import HTTPStatus

from ..models.UserModel import UserModel
from ..services.auth import hash_password, check_password

login_api = Blueprint('login', __name__)

black_list = set()


@login_api.route('/login', methods=['POST'])
def login():
    data = request.get_json()

    email = data.get('email')
    password = data.get('password')

    user = UserModel.get_by_email(email=email)

    if not user or not check_password(password, user.password):
        return {'message': 'Invalid Credentials'}, HTTPStatus.BAD_REQUEST

    access_token = create_access_token(identity=user.id)
    refresh_token = create_refresh_token(identity=user.id)

    return {
        'message': 'success',
        'access_token': access_token,
        'refresh_token': refresh_token
    }, HTTPStatus.OK


@login_api.route('/logout', methods=['POST'])
@jwt_required()
def logout():
    # return 'loggin out'
    jti = get_jwt()['jti']

    black_list.add(jti)

    return {'message': 'successfully logged out'}, HTTPStatus.OK


@login_api.route('/refresh_token', methods=['POST'])
def refresh_logout():
    return 'refreshing'