from passlib.hash import pbkdf2_sha256
# from flask import request
# from flask_jwt_extended import  create_access_token
# from ..models.user import User


def hash_password(password):
    return pbkdf2_sha256.hash(password)


def check_password(password, hashed):
    return pbkdf2_sha256.verify(password, hashed)




