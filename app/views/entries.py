from app.models.dbtasks import Profile, UserOperations
from app.schemas.entries import (entries_schema,
                                 process_entry_json)
from app.utils.authentication import token_header
from flask import Blueprint, jsonify, make_response, request

database = UserOperations()

url_prefix = '/api/v1/entries'
entries = Blueprint('entries', __name__, url_prefix=url_prefix)


@entries.route('', methods=['GET'])
@token_header
def get_all_entries(user_id):
    """
    End Point get all entries for a user
    """
    resultlist = database.get_all_entries(user_id)
    return make_response(jsonify({'entries': resultlist})), 200


@entries.route('', methods=['POST'])
@token_header
def make_new_entry(user_id):
    """
    End Point to create an entry
    """
    if request.method == "POST":
        data = process_entry_json(request.json)
        entry = database.make_an_entry(
            user_id, data['entry_date'], data['entry_name'],
            data['entry_content'])
    return make_response(jsonify({'message': 'entry created',
                                  "entry_id": entry["entry_id"]})), 201


@entries.route('/<int:entry_no>', methods=['GET'])
@token_header
def single_entry(user_id, entry_no):
    """
    End Point to get an single entry
    """
    resultlist = database.get_one_entry(user_id, entry_no)
    if resultlist:
        return make_response(jsonify({'entries': resultlist})), 200
    else:
        return make_response(jsonify({'message': 'no entry'})), 404


@entries.route('/<int:entry_no>', methods=['PUT'])
@token_header
def edit_an_entry_(user_id, entry_no):
    """
    End Point to edit an existing entry
    """
    data = process_entry_json(request.json, partial=True)
    resultlist = database.get_one_entry(user_id, entry_no)

    if resultlist:
        resultlist.update(data)
        database.edit_one_entry(user_id, **resultlist)
        return make_response(jsonify({'message': 'entry edited'})), 200
    else:
        return make_response(jsonify({'message': 'no such entry'})), 404


@entries.route('/<int:entry_no>', methods=['DELETE'])
@token_header
def delete_an_entry(user_id, entry_no):
    """
    End Point to delete an existing entry
    """

    message = database.delete_entry(user_id, entry_no)
    return make_response(jsonify({'message': message})), 200
