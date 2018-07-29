from flask import Flask, jsonify, make_response, request
import datetime
from api.v1.models import dbase
from werkzeug.security import generate_password_hash, check_password_hash
from api.v1.dbtasks import dboperations
import json
import jwt


# example entries
entries = []
app = Flask(__name__)
app.config['SECRET_KEY'] = 'tisandela'
database = dboperations()


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
            'entry_id': var['entry_id'],
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


@app.route('/api/v1/auth/signup', methods=['POST'])
def create_a_user():
    data = process_json(request.json, 'user')
    hashed_password = generate_password_hash(data['password'], method='sha256')
    database.create_a_user(
        data['username'], data['name'], data['email'], hashed_password)
    return make_response(jsonify({'Message': 'User created'})), 200


# @app.route('/api/v1/auth/signout', methods=['POST'])
# def signout_a_user():
#     data = process_json(request.json)
#     return make_response(jsonify({'Message': 'User logged out'})), 200


@app.route('/api/v1/auth/login')
def sign_in_a_user():
    user = database.select_user('simon')
    return jsonify({'mesage':user})
    # auth = request.authorization
    # if not auth or not auth.username or not auth.password:
    #     return make_response(jsonify({'Invalid login': 'try again'}), 401)

    # user = database.select_user(auth.username)
    # if not user:
    #     return make_response(jsonify({'Invalid login': 'try again'}), 401)

    # if check_password_hash(user['password'], auth.password):
    #     token = jwt.encode({'public_id': user['user_id'], 'exp': datetime.datetime.utcnow(
    #     )+datetime.timedelta(minutes=20)}, app.config['SECRET_KEY'])
    #     return jsonify({'token':token.decode('UTF-8')})
    # return make_response(jsonify({'Invalid login': 'try again'}), 401)
    


@app.route('/')
def index():
    return jsonify({'hello': 'world'}), 200


@app.route('/api/v1/entries', methods=['GET'])
def get_all_entries():
    resultlist = database.get_all_entries()
    return make_response(jsonify({'entries': resultlist})), 200


@app.route('/api/v1/entries', methods=['POST'])
def make_new_entry():
    if request.method == "POST":
        data = process_json(request.json, 'entry')
        database.make_an_entry(
            data['entry_id'], data['entry_date'], data['entry_name'], data['entry_content'])
    return make_response(jsonify({'Message': 'entry created'})), 200


@app.route('/api/v1/entries/<int:entry_no>', methods=['GET'])
def single_entry(entry_no):
    resultlist = database.get_one_entry(entry_no)
    if resultlist:
        return make_response(jsonify({'entries': resultlist})), 200
    else:
        return make_response(jsonify({'Message': 'no entry'})), 404


@app.route('/api/v1/entries/<int:entry_no>', methods=['PUT'])
def edit_an_entry_(entry_no):
    data = process_json(request.json, 'edit')
    database.edit_one_entry(
        data['entry_name'], data['entry_content'], entry_no)
    return make_response(jsonify({'Message': 'entry edited'})), 200
