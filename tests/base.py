"""Base module with test helper functions"""
import io
import json
import os
import unittest
from app.models.dbtasks import Profile, UserOperations
from app.utils.fixtures import create_tables
from config import app_config
from tests import (test_entry, test_sign_in, test_user_data,
                   test_wrong_sign_in, wrong_test_entry, wrong_test_sign_in,
                   wrong_test_user_data)

from app import app, db

database = UserOperations()


class TestingClass(unittest.TestCase):

    """Base Class for Testing the API"""

    def setUp(self):
        self.app = app
        self.app.config.from_object(app_config.get('testing'))
        self.app.testing = True
        # change test db
        db_url = app.config.get('TEST_DATABASE_URL')
        db.get_connection(db_url, auto_commit=True)
        create_tables()
        self.test_user = self.app.test_client()

    def tearDown(self):
        clear_user_table = "DELETE from users CASCADE"
        database.cursor.execute(clear_user_table)


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
    """Function test login with missing login info"""
    response = test_user.post(
        "/api/v1/auth/login", data=json.dumps(wrong_test_sign_in),
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


def profile(test_user):
    """Function to test retruning profile"""
    response = test_user.get('/api/v1/profile',
                             headers=user_create_token(test_user),
                             content_type='application/json')
    return response


def edit_profession(test_user):
    """Function to test edit profile profession"""
    response = test_user.put('/api/v1/profile',
                             headers=user_create_token(test_user),
                             data=json.dumps({'profession': 'Simon'}),
                             content_type='application/json')
    return response


def edit(test_user):
    """Function to test no parameter sent to edit profile"""
    response = test_user.put('/api/v1/profile',
                             headers=user_create_token(test_user),
                             content_type='application/json')
    return response


def pic_upload(test_user):
    """Function to test add pic"""
    data = {}
    data['photo'] = (io.BytesIO(b'test'), 'test_file.jpg')
    response = test_user.post('/api/v1/profile/pic',
                              headers=user_create_token(test_user),
                              data=data,
                              content_type='multipart/form-data')
    return response


def pic_no_upload(test_user):
    """Function to test not add pic"""
    response = test_user.post('/api/v1/profile/pic',
                              headers=user_create_token(test_user),
                              data=json.dumps({"path": ""}),
                              content_type='application/json')
    return response


def pic_not_added_upload(test_user):
    """Function to test add not pic"""
    data = {}
    response = test_user.post('/api/v1/profile/pic',
                              headers=user_create_token(test_user),
                              data=data,
                              content_type='multipart/form-data')
    return response


if __name__ == '__main__':
    unittest.main()
