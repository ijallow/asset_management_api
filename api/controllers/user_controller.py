from flask import Flask, request, jsonify, make_response, Blueprint
from flask_jwt_extended import create_access_token, get_jwt_identity, jwt_required

from ..models.user import User, UserSchema
from ..services.auth import hash_password, check_password

user_api = Blueprint('users', __name__)

User_schema = UserSchema(many=True)
user_schema = UserSchema()


# for getting all users
@user_api.route('/users', methods=["GET"])
def get_all_users():
    users = User.query.all()
    if users:
        output = []
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
    data = request.get_json()

    username = data.get('username')
    email = data.get('email')
    non_hash_password = data.get('password')

    if User.get_by_username(username):
        return {'message': 'username already used'}

    if User.get_by_email(email):
        return {'message': 'email already used'}

    password = hash_password(non_hash_password)

    user = User(
        username=username,
        email=email,
        password=password
    )

    user.save()

    output = []

    data = {
        'id': user.id,
        'username': user.username,
        'email': user.email
    }

    output.append(data)

    return jsonify({'user', output}),


# for loggin in users
@user_api.route('/users/login', methods=['POST'])
def login():
    data = request.get_json()

    email = data.get('email')
    password = data.get('password')

    user = User.get_by_email(email=email)

    if not user or not check_password(password, user.password):
        return {'message': 'email or password is incorrect'}

    access_token = create_access_token(identity=user.id)

    return {'access_token': access_token}


@user_api.route('/users/<string:username>', methods=['GET'])
@jwt_required(optional=True)
def get_user(username):
    user = User.get_by_username(username=username)

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
