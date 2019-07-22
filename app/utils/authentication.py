import datetime
from functools import wraps

from flask import make_response, request, jsonify, current_app

import jwt
from app.models.dbtasks import Profile, UserOperations

database = UserOperations()


def token_header(f):
    ''' Function to get the token using the header'''
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        if 'token' in request.headers:
            token = request.headers['token']

        if not token:
            return make_response(jsonify({'message': 'No auth token'}), 401)
        try:
            data = jwt.decode(
                token, current_app.config['SECRET_KEY'], algorithm=['HS256'])
            user = database.select_user_id(data['user_id'])
            user_id = user[0]['user_id']
        except:
            return make_response(jsonify({'message': 'Invalid token'}), 401)
        return f(user_id, *args, **kwargs)
    return decorated


def generate_token(user):
    token = jwt.encode({'user_id': user[0]['user_id'],
                        'exp': datetime.datetime.utcnow() +
                        datetime.timedelta(minutes=60)},
                       current_app.config['SECRET_KEY'], algorithm='HS256')
    return token
