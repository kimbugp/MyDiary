from flask import Flask, jsonify, make_response, request
import datetime
from api.v1.models import dbase
from werkzeug.security import generate_password_hash, check_password_hash
from api.v1.dbtasks import dboperations
import json
import jwt
from functools import wraps


app = Flask(__name__)
app.config['SECRET_KEY'] = 'tisandela'
database = dboperations()


''' Function to process json recieved from browser'''


def process_json(var, id):
    if id == 'user':
        user = {
            'username': var['username'],
            'name': var['name'],
            'email': var['email'],
            'password': var['password']
        }
        return user
    elif id == 'entry':
        now = datetime.datetime.now()
        entry = {
            'entry_date': now.strftime("%Y-%m-%d %H:%M"),
            'entry_name': var['entry_name'],
            'entry_content': var['entry_content']
        }
        return entry
    elif id == 'edit':
        entry = {
            'entry_name': var['entry_name'],
            'entry_content': var['entry_content']
        }
        return entry
    elif id == 'signin':
        user = {
            'username': var['username'],
            'password': var['password']
        }
        return user


''' Function to get the token using the header'''


def token_header(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        if 'token' in request.headers:
            token = request.headers['token']

        if not token:
            return make_response(jsonify({'message': 'No auth token'}), 401)
        try:
            data = jwt.decode(token, app.config['SECRET_KEY'])
            user = database.select_user_id(data['user_id'])
            user_id = user[0]['user_id']
        except:
            return make_response(jsonify({'message': 'Invalid token'}), 401)
        return f(user_id, *args, **kwargs)
    return decorated


"""
End Point to create an account for a user
"""


@app.route('/api/v1/auth/signup', methods=['POST'])
def create_a_user():
    data = process_json(request.json, 'user')
    hashed_password = generate_password_hash(data['password'], method='sha256')
    database.create_a_user(
        data['username'], data['name'], data['email'], hashed_password)
    return make_response(jsonify({'Message': 'User created'})), 200


"""
End Point to log a user into their account
"""


@app.route('/api/v1/auth/login', methods=['POST'])
def sign_in_a_user():
    data = process_json(request.json, 'signin')
    user = database.select_user(data['username'])
    # import pdb; pdb.set_trace()
    if user:
        if check_password_hash(user[0]['password'], data['password']):
            token = jwt.encode({'user_id': user[0]['user_id'], 'exp': datetime.datetime.utcnow(
            )+datetime.timedelta(minutes=20)}, app.config['SECRET_KEY'])
            return jsonify({'Token': token.decode('UTF-8')})
        else:
            return make_response(jsonify({'Message': 'Invalid login'}), 401)
    else:
        return make_response(jsonify({'Message': 'Invalid login'}), 401)


"""
End Point for the index page
"""


@app.route('/')
def index():
    return jsonify({'hello': 'world'}), 200


"""
End Point get all entries for a user
"""


@app.route('/api/v1/entries', methods=['GET'])
@token_header
def get_all_entries(user_id):
    resultlist = database.get_all_entries(user_id)
    return make_response(jsonify({'entries': resultlist})), 200


"""
End Point to create an entry
"""


@app.route('/api/v1/entries', methods=['POST'])
@token_header
def make_new_entry(user_id):
    if request.method == "POST":
        data = process_json(request.json, 'entry')
        database.make_an_entry(
            user_id, data['entry_date'], data['entry_name'], data['entry_content'])
    return make_response(jsonify({'Message': 'entry created'})), 200


"""
End Point to get an single entry
"""


@app.route('/api/v1/entries/<int:entry_no>', methods=['GET'])
@token_header
def single_entry(user_id,entry_no):
    resultlist = database.get_one_entry(user_id,entry_no)
    if resultlist:
        return make_response(jsonify({'entries': resultlist})), 200
    else:
        return make_response(jsonify({'Message': 'no entry'})), 404


"""
End Point to edit an existing entry
"""


@app.route('/api/v1/entries/<int:entry_no>', methods=['PUT'])
@token_header
def edit_an_entry_(user_id,entry_no):
    data = process_json(request.json, 'edit')
    resultlist = database.get_one_entry(user_id,entry_no)
    if resultlist:
        database.edit_one_entry(
            data['entry_name'], data['entry_content'], entry_no)
        return make_response(jsonify({'Message': 'entry edited'})), 200
    else:
        return make_response(jsonify({'Message': 'no such entry'})), 200


"""
End Point to delete an existing entry
"""


@app.route('/api/v1/entries/<int:entry_no>', methods=['DELETE'])
@token_header
def delete_an_entry(user_id,entry_no):
    message = database.delete_entry(entry_no)
    return make_response(jsonify({'Message': message})), 200
