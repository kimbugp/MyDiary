"""Main API"""
import datetime
from functools import wraps
import re
import jwt
from pyisemail import is_email
from werkzeug.security import generate_password_hash, check_password_hash
from flask import Flask, jsonify, make_response, request, redirect
from api.v1.models import dbase
from api.v1.dbtasks import dboperations


app = Flask(__name__)
db = dbase()
db.create_user_table()
db.create_entries_table()
app.config['SECRET_KEY'] = 'tisandela'
database = dboperations()


def process_json(var, process_id):
    ''' Function to process json recieved from browser'''
    if process_id == 'user':
        try:
            user = {
                'username': var['username'],
                'name': var['name'],
                'email': var['email'],
                'password': var['password']
            }
            return user
        except:
            error = "parameter missing"
            return error
    elif process_id == 'entry':
        try:
            now = datetime.datetime.now()
            entry = {
                'entry_date': now.strftime("%Y-%m-%d %H:%M"),
                'entry_name': var['entry_name'],
                'entry_content': var['entry_content']
            }
            return entry
        except:
            error = "parameter missing"
            return error
    elif process_id == 'edit':
        try:
            entry = {
                'entry_name': var['entry_name'],
                'entry_content': var['entry_content']
            }
            return entry
        except:
            error = "parameter missing"
            return error

    elif process_id == 'signin':
        try:
            user = {
                'username': var['username'],
                'password': var['password']
            }
            return user
        except:
            error = "parameter missing"
            return error


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
            data = jwt.decode(token, app.config['SECRET_KEY'])
            user = database.select_user_id(data['user_id'])
            user_id = user[0]['user_id']
        except:
            return make_response(jsonify({'message': 'Invalid token'}), 401)
        return f(user_id, *args, **kwargs)
    return decorated


@app.route('/api/v1/auth/signup', methods=['POST'])
def create_a_user():
    """
    End Point to create an account for a user
    """
    data = process_json(request.json, 'user')
    if data == "parameter missing":
        return make_response(jsonify({'message': 'parameter missing'}), 400)
    hashed_password = generate_password_hash(data['password'], method='sha256')
    user = database.verify_new_user(data['username'], data['email'])
    if not user and is_email(data['email']) and all(data.values()) and re.match("^[A-Za-z0-9_-]*$", data['username']):
        database.create_a_user(
            data['username'], data['name'], data['email'], hashed_password)
        return make_response(jsonify({'Message': 'User created'})), 201
    elif not is_email(data['email']):
        return make_response(jsonify({'Message': 'invalid email'}), 400)
    elif not all(data.values()) or not re.match("^[A-Za-z0-9_-]*$", data['username']):
        return make_response(jsonify({'Message': 'invalid input'}), 400)
    return make_response(jsonify({'Message': 'User already exists'}), 400)


@app.route('/api/v1/auth/login', methods=['POST'])
def sign_in_a_user():
    """
    End Point to log a user into their account
    """
    data = process_json(request.json, 'signin')
    if data == "parameter missing":
        return make_response(jsonify({'message': 'parameter missing'}), 400)
    user = database.select_user(data['username'])
    # import pdb; pdb.set_trace()
    if user:
        if check_password_hash(user[0]['password'], data['password']):
            token = jwt.encode({'user_id': user[0]['user_id'], 'exp': datetime.datetime.utcnow() +
                                datetime.timedelta(minutes=20)},
                               app.config['SECRET_KEY'])
            return make_response(jsonify({'Token': token.decode('UTF-8')}), 200)
        else:
            return make_response(jsonify({'Message': 'Check your login'}), 401)
    else:
        return make_response(jsonify({'Message': 'Invalid login'}), 401)


@app.route('/')
def index():
    """
    End Point for the index page
    """
    return jsonify({'hello': 'world'}), 200


@app.route('/api/v1/entries', methods=['GET'])
@token_header
def get_all_entries(user_id):
    """
    End Point get all entries for a user
    """
    resultlist = database.get_all_entries(user_id)
    return make_response(jsonify({'entries': resultlist})), 200


@app.route('/api/v1/entries', methods=['POST'])
@token_header
def make_new_entry(user_id):
    """
    End Point to create an entry
    """
    if request.method == "POST":
        data = process_json(request.json, 'entry')
        if data == "parameter missing" or not all(data.values()):
            return make_response(jsonify({'message': 'parameter missing'}), 400)
        database.make_an_entry(
            user_id, data['entry_date'], data['entry_name'],
            data['entry_content'])
    return make_response(jsonify({'Message': 'entry created'})), 201


@app.route('/api/v1/entries/<int:entry_no>', methods=['GET'])
@token_header
def single_entry(user_id, entry_no):
    """
    End Point to get an single entry
    """

    resultlist = database.get_one_entry(user_id, entry_no)
    if resultlist:
        return make_response(jsonify({'entries': resultlist})), 200
    else:
        return make_response(jsonify({'Message': 'no entry'})), 404


@app.route('/api/v1/entries/<int:entry_no>', methods=['PUT'])
@token_header
def edit_an_entry_(user_id, entry_no):
    """
    End Point to edit an existing entry
    """
    data = process_json(request.json, 'edit')
    if data == "parameter missing":
        return make_response(jsonify({'message': 'parameter missing'}), 400)
    resultlist = database.get_one_entry(user_id, entry_no)
    if resultlist:
        database.edit_one_entry(
            user_id, data['entry_name'], data['entry_content'], entry_no)
        return make_response(jsonify({'Message': 'entry edited'})), 200
    else:
        return make_response(jsonify({'Message': 'no such entry'})), 404


@app.route('/api/v1/entries/<int:entry_no>', methods=['DELETE'])
@token_header
def delete_an_entry(user_id, entry_no):
    """
    End Point to delete an existing entry
    """

    message = database.delete_entry(user_id, entry_no)
    return make_response(jsonify({'Message': message})), 200


@app.errorhandler(404)
def page_not_found(e):
    """
    End Point to catch 404s
    """
    return make_response(jsonify({'Message': 'Page not found'})), 404


@app.route('/docs')
def documentation():
    """
    End Point for documentation
    """
    return redirect('https://kimbug.docs.apiary.io', code=302)


@app.route('/api/v1/profile', methods=['GET'])
@token_header
def view_profile(user_id):
    """
    End Point to view user profile
    """
    response = database.get_profile(user_id)
    return make_response(jsonify(response), 200)
