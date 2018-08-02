import unittest
from flask import Flask, jsonify, make_response, request
import sys
import json

from api import app
from api.v1.models import dbase
from api.v1.dbtasks import dboperations
from tests import *

database = dboperations()
db = dbase()
cursor = db.cursor

class TestingClass(unittest.TestCase):

    def setUp(self):
        self.test_user=app.test_client(self)

    def tearDown(self):
        clear_user_table = "DELETE from users"
        cursor.execute(clear_user_table)
        clear_user_table = "DELETE from entries"
        cursor.execute(clear_user_table)

def user_create_token(test_user):
    test_user.post(
            "/api/v1/auth/signup", data=json.dumps(test_user_data), content_type="application/json")
    response = test_user.post('/api/v1/auth/login',
                                  data=json.dumps(test_sign_in),
                                  content_type='application/json')
    token = response.json
    return token
def user_create(test_user):
    response=test_user.post(
            "/api/v1/auth/signup", data=json.dumps(test_user_data), content_type="application/json")
    return response
def wrong_details(test_user):
    response=test_user.post(
            "/api/v1/auth/signup", data=json.dumps(wrong_test_sign_in), content_type="application/json")
    return response

def create_an_entry(test_user):
    response=test_user.post('/api/v1/entries', headers=user_create_token(test_user),
                       data=json.dumps(test_entry),
                       content_type='application/json')
    return response

def get_an_entry(test_user):
    response =test_user.get(
            "/api/v1/entries", headers=user_create_token(test_user), content_type="application/json")
    return response
def wrong_user(test_user):
    response =test_user.post(
            "/api/v1/auth/signup", data=json.dumps(wrong_test_user_data), content_type="application/json")
    return response

def create_wrong_entry(test_user):
    response = test_user.post('/api/v1/entries', headers=user_create_token(test_user),
                                  data=json.dumps(wrong_test_entry),
                                  content_type='application/json')
    return response

def get_single_entry(test_user):
    my_id = database.get_an_id()
    response = test_user.get('/api/v1/entries/{}'.format(my_id), headers=user_create_token(test_user),
                                 content_type='application/json')
    return response
def no_existing_entry(test_user):
    response =test_user.get(
            "/api/v1/entries/1", headers=user_create_token(test_user), content_type="application/json")
    return response

def edit_entry(test_user):
    create_an_entry(test_user)
    my_id = database.get_an_id()
    response=test_user.put('/api/v1/entries/{}'.format(my_id), headers=user_create_token(test_user),
                       data=json.dumps(test_entry),
                       content_type='application/json')
    return response

def delete_entry(test_user):
    create_an_entry(test_user)
    my_id = database.get_an_id()
    response=test_user.delete('/api/v1/entries/{}'.format(my_id), headers=user_create_token(test_user),
                       data=json.dumps(test_entry),
                       content_type='application/json')
    return response

def no_token(test_user):
    create_an_entry(test_user)
    my_id = database.get_an_id()
    response=test_user.put('/api/v1/entries/{}'.format(my_id),
                       data=json.dumps(test_entry),
                       content_type='application/json')
    return response

def wrong_token(test_user):
    create_an_entry(test_user)
    my_id = database.get_an_id()
    response=test_user.put('/api/v1/entries/{}'.format(my_id),headers={"token": "ddddd"},
                       data=json.dumps(test_entry),
                       content_type='application/json')
    return response
def wrong_sign_in(test_user):
    response=test_user.post(
            "/api/v1/auth/login", data=json.dumps(test_wrong_sign_in), content_type="application/json")
    return response

def edit_no_entry(test_user):
    create_an_entry(test_user)
    response=test_user.put('/api/v1/entries/1', headers=user_create_token(test_user),
                       data=json.dumps(test_entry),
                       content_type='application/json')
    return response
def wrong_data(test_user):
    create_an_entry(test_user)
    my_id = database.get_an_id()
    response=test_user.put('/api/v1/entries/{}'.format(my_id),headers=user_create_token(test_user),
                       data=json.dumps(wrong_test_entry),
                       content_type='application/json')
    return response
def helo(test_user):
    response=test_user.get('/', content_type="application/json")
    return response