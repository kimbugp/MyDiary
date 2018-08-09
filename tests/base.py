"""Base module with test helper functions"""
import unittest
import json

from api import app
from api.v1.models import dbase
from api.v1.dbtasks import dboperations
from tests import (test_user_data, test_sign_in, test_entry, wrong_test_entry,
                   wrong_test_user_data, wrong_test_sign_in, test_wrong_sign_in)
app.config["testing"] = True
database = dboperations()
db = dbase()
cursor = db.cursor


class TestingClass(unittest.TestCase):

    """Base Class for Testing the API"""

    def setUp(self):
        self.test_user = app.test_client(self)
        

    def tearDown(self):
        clear_user_table = "DELETE from users CASCADE"
        cursor.execute(clear_user_table)
        # clear_user_table = "DELETE from entries"
        # cursor.execute(clear_user_table)


def user_create_token(test_user):
    """FUnction to create login token"""
    test_user.post(
        "/api/v1/auth/signup", data=json.dumps(
            test_user_data), content_type="application/json")
    response = test_user.post('/api/v1/auth/login',
                              data=json.dumps(test_sign_in),
                              content_type='application/json')
    token = response.json
    return token


def user(test_user):
    """FUnction to signin"""
    test_user.post(
        "/api/v1/auth/signup", data=json.dumps(
            test_user_data), content_type="application/json")
    response = test_user.post('/api/v1/auth/login',
                              data=json.dumps(test_sign_in),
                              content_type='application/json')
    return response


def user_create(test_user):
    """Function to create a user"""
    response = test_user.post(
        "/api/v1/auth/signup", data=json.dumps(test_user_data),
        content_type="application/json")
    return response


def wrong_details(test_user):
    """Function test wrong login details"""
    response = test_user.post(
        "/api/v1/auth/signup", data=json.dumps(wrong_test_sign_in),
        content_type="application/json")
    return response


def create_an_entry(test_user):
    """Function to create an entry"""
    response = test_user.post('/api/v1/entries',
                              headers=user_create_token(test_user),
                              data=json.dumps(test_entry),
                              content_type='application/json')
    return response


def get_an_entry(test_user):
    """Function to all get an entry"""
    response = test_user.get(
        "/api/v1/entries", headers=user_create_token(test_user),
        content_type="application/json")
    return response


def wrong_user(test_user):
    """Function to test wrong user input"""
    response = test_user.post(
        "/api/v1/auth/signup", data=json.dumps(wrong_test_user_data),
        content_type="application/json")
    return response


def create_wrong_entry(test_user):
    """Function to test wrong user entry input"""
    response = test_user.post('/api/v1/entries',
                              headers=user_create_token(test_user),
                              data=json.dumps(wrong_test_entry),
                              content_type='application/json')
    return response


def get_single_entry(test_user):
    """Function to all get an entry"""
    my_id = database.get_an_id()
    response = test_user.get('/api/v1/entries/{}'.format(my_id),
                             headers=user_create_token(test_user),
                             content_type='application/json')
    return response


def no_existing_entry(test_user):
    """Function to test non exisitng entry"""
    response = test_user.get(
        "/api/v1/entries/1", headers=user_create_token(test_user),
        content_type="application/json")
    return response


def edit_entry(test_user):
    """Function to test editing an entry"""
    create_an_entry(test_user)
    my_id = database.get_an_id()
    response = test_user.put('/api/v1/entries/{}'.format(my_id),
                             headers=user_create_token(test_user),
                             data=json.dumps(test_entry),
                             content_type='application/json')
    return response


def delete_entry(test_user):
    """Function to test deleting an entry"""
    create_an_entry(test_user)
    my_id = database.get_an_id()
    response = test_user.delete('/api/v1/entries/{}'.format(my_id),
                                headers=user_create_token(test_user),
                                data=json.dumps(test_entry),
                                content_type='application/json')
    return response


def no_token(test_user):
    """Function to test operation with no token"""
    create_an_entry(test_user)
    my_id = database.get_an_id()
    response = test_user.put('/api/v1/entries/{}'.format(my_id),
                             data=json.dumps(test_entry),
                             content_type='application/json')
    return response


def wrong_token(test_user):
    """Function to test operation with wrong token"""
    create_an_entry(test_user)
    my_id = database.get_an_id()
    response = test_user.put('/api/v1/entries/{}'.format(my_id),
                             headers={"token": "ddddd"},
                             data=json.dumps(test_entry),
                             content_type='application/json')
    return response


def wrong_sign_in(test_user):
    """Function to test sign in with wrong details"""
    response = test_user.post(
        "/api/v1/auth/login", data=json.dumps(test_wrong_sign_in),
        content_type="application/json")
    return response


def edit_no_entry(test_user):
    """Function to test trying to edit non existng entry"""
    create_an_entry(test_user)
    response = test_user.put('/api/v1/entries/1',
                             headers=user_create_token(test_user),
                             data=json.dumps(test_entry),
                             content_type='application/json')
    return response


def wrong_data(test_user):
    """Function to test trying make wrong entry"""
    create_an_entry(test_user)
    my_id = database.get_an_id()
    response = test_user.put('/api/v1/entries/{}'.format(my_id),
                             headers=user_create_token(test_user),
                             data=json.dumps(wrong_test_entry),
                             content_type='application/json')
    return response


def helo(test_user):
    """Function to test hello world"""
    response = test_user.get('/', content_type="application/json")
    return response

def error_page(test_user):
    """Function to test 404 errors"""
    response = test_user.get('/3/', content_type="application/json")
    return response
