from flask import request, jsonify, Blueprint
from flask_jwt_extended import (create_access_token,
                                get_jwt_identity,
                                jwt_required,
                                create_refresh_token,
                                get_jwt)
from http import HTTPStatus

from ..models.UserModel import UserModel, UserSchema
from ..services.auth import hash_password, check_password, login_service

user_api = Blueprint('users', __name__)

users_schema = UserSchema(many=True)
user_schema = UserSchema()


# for getting all users
@user_api.route('/users', methods=["GET"])
def get_all_users():
    users = UserModel.query.all()
    output = []
    if users:

        for user in users:
            data = {
                'username': user.username,
                'email': user.email,
                # 'password': user.password
            }
            output.append(data)
    return jsonify({'users': output})


# for adding a user
@user_api.route('/users', methods=['POST'])
def create_user():
    json_data = request.get_json()

    username = json_data.get('username')
    email = json_data.get('email')
    non_hash_password = json_data.get('password')

    if UserModel.get_by_username(username):
        return {'message': 'username already used'}

    if UserModel.get_by_email(email):
        return {'message': 'email already used'}

    password = hash_password(non_hash_password)

    user = UserModel(username=username, email=email, password=password)
    user.save()

    data = {
        'id': user.id,
        'username': user.username,
        'email': user.email
    }

    return jsonify({'user': data})


@user_api.route('/users/<string:username>', methods=['GET'])
@jwt_required(optional=True)
def get_user(username):
    user = UserModel.get_by_username(username=username)

    if user is None:
        return {'message': 'user not found'}

    current_user = get_jwt_identity()

    if current_user == user.id:
        data = {
            'id': user.id,
            'username': user.username,
            'email': user.email
        }
    else:
        data = {
            'id': user.id,
            'username': user.username,
        }

    return user_schema.jsonify(data)




