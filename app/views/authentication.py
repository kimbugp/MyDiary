import datetime
import re

from werkzeug.security import check_password_hash, generate_password_hash

from app.models.dbtasks import UserOperations
from app.schemas.users import process_signin_json, process_user_json
from app.utils.authentication import generate_token
from flask import Blueprint, jsonify, make_response, request

database = UserOperations()

url_prefix = '/api/v1/auth'
auth = Blueprint('authentication', __name__, url_prefix=url_prefix)


@auth.route('/signup', methods=['POST'])
def create_a_user():
    """
    End Point to create an account for a user
    """
    data = request.json
    process_user_json(data)
    hashed_password = generate_password_hash(data['password'], method='sha256')
    user = database.verify_new_user(data['username'], data['email'])
    if not user:
        database.create_a_user(
            data['username'], data['name'], data['email'], hashed_password)
        return make_response(jsonify({'message': 'User created'})), 201
    return make_response(jsonify({'message': 'User already exists'}), 400)


@auth.route('login', methods=['POST'])
def sign_in_a_user():
    """
    End Point to log a user into their account
    """

    data = request.json
    process_signin_json(data)
    if data == "parameter missing":
        return make_response(jsonify({'message': 'parameter missing'}), 400)
    user = database.select_user(data['username'])
    if user:
        if check_password_hash(user[0]['password'], data['password']):
            token = generate_token(user)
            return make_response(jsonify({'Token': token.decode('UTF-8')}), 200)
    return make_response(jsonify({'message': 'Invalid login'}), 401)
