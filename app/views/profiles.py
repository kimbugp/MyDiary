"""Profiles view"""
import os

from flask import Flask, jsonify, make_response, request, Blueprint

from app.models.dbtasks import Profile
from app.utils.authentication import token_header

prof = Profile()

url_prefix = '/api/v1/profile'
profile = Blueprint('profiles', __name__, url_prefix=url_prefix)


@profile.route('', methods=['GET'])
@token_header
def view_profile(user_id):
    """
    End Point to view user profile
    """
    response = prof.get_profile(user_id)
    return make_response(jsonify(response), 200)


@profile.route('', methods=['PUT'])
@token_header
def edit(user_id):
    """
    End Point to edit user profile
    """
    data = request.json
    if 'profession' in data and all(data.values()):
        prof.edit_profile(user_id, data['profession'])
        return make_response(jsonify({"message": "edited"}), 200)
    return make_response(jsonify({"message": "parameter  missing"}), 400)
