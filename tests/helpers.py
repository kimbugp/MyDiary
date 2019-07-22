import json
from tests import (test_entry, test_sign_in, test_user_data,
                   test_wrong_sign_in, wrong_test_entry, wrong_test_sign_in,
                   wrong_test_user_data)


class Helpers():
    def __init__(self, test_user):
        self.test_user = self.test_user

    def user_create_token(self):
        """FUnction to create login token"""
        self.test_user.post(
            "/api/v1/auth/signup", data=json.dumps(
                test_user_data), content_type="application/json")
        response = self.test_user.post('/api/v1/auth/login',
                                       data=json.dumps(test_sign_in),
                                       content_type='application/json')
        token = response.json
        return token

    def user(self):
        """FUnction to signin"""
        self.test_user.post(
            "/api/v1/auth/signup", data=json.dumps(
                test_user_data), content_type="application/json")
        response = self.test_user.post('/api/v1/auth/login',
                                       data=json.dumps(test_sign_in),
                                       content_type='application/json')
        return response

    def user_create(self):
        """Function to create a user"""
        response = self.test_user.post(
            "/api/v1/auth/signup", data=json.dumps(test_user_data),
            content_type="application/json")
        return response

    def wrong_details(self):
        """Function test login with missing login info"""
        response = self.test_user.post(
            "/api/v1/auth/login", data=json.dumps(wrong_test_sign_in),
            content_type="application/json")
        return response

    def create_an_entry(self):
        """Function to create an entry"""
        response = self.test_user.post('/api/v1/entries',
                                       headers=self.user_create_token(),
                                       data=json.dumps(test_entry),
                                       content_type='application/json')
        return response

    def get_an_entry(self):
        """Function to all get an entry"""
        response = self.test_user.get(
            "/api/v1/entries", headers=self.user_create_token(),
            content_type="application/json")
        return response

    def wrong_user(self):
        """Function to test wrong user input"""
        response = self.test_user.post(
            "/api/v1/auth/signup", data=json.dumps(wrong_test_user_data),
            content_type="application/json")
        return response

    def create_wrong_entry(self):
        """Function to test wrong user entry input"""
        response = self.test_user.post('/api/v1/entries',
                                       headers=self.user_create_token(),
                                       data=json.dumps(wrong_test_entry),
                                       content_type='application/json')
        return response

    def get_single_entry(self):
        """Function to all get an entry"""
        my_id = self.database.get_an_id()
        response = self.test_user.get('/api/v1/entries/{}'.format(my_id),
                                      headers=self.user_create_token(),
                                      content_type='application/json')
        return response

    def no_existing_entry(self):
        """Function to test non exisitng entry"""
        response = self.test_user.get(
            "/api/v1/entries/1", headers=self.user_create_token(),
            content_type="application/json")
        return response

    def edit_entry(self):
        """Function to test editing an entry"""
        self.create_an_entry()
        my_id = self.database.get_an_id()
        response = self.test_user.put('/api/v1/entries/{}'.format(my_id),
                                      headers=self.user_create_token(),
                                      data=json.dumps(test_entry),
                                      content_type='application/json')
        return response

    def delete_entry(self):
        """Function to test deleting an entry"""
        self.create_an_entry()
        my_id = self.database.get_an_id()
        response = self.test_user.delete('/api/v1/entries/{}'.format(my_id),
                                         headers=self.user_create_token(),
                                         data=json.dumps(test_entry),
                                         content_type='application/json')
        return response

    def no_token(self):
        """Function to test operation with no token"""
        self.create_an_entry()
        my_id = self.database.get_an_id()
        response = self.test_user.put('/api/v1/entries/{}'.format(my_id),
                                      data=json.dumps(test_entry),
                                      content_type='application/json')
        return response

    def wrong_token(self):
        """Function to test operation with wrong token"""
        self.create_an_entry()
        my_id = self.database.get_an_id()
        response = self.test_user.put('/api/v1/entries/{}'.format(my_id),
                                      headers={"token": "ddddd"},
                                      data=json.dumps(test_entry),
                                      content_type='application/json')
        return response

    def wrong_sign_in(self):
        """Function to test sign in with wrong details"""
        response = self.test_user.post(
            "/api/v1/auth/login", data=json.dumps(test_wrong_sign_in),
            content_type="application/json")
        return response

    def edit_no_entry(self):
        """Function to test trying to edit non existng entry"""
        self.create_an_entry()
        response = self.test_user.put('/api/v1/entries/1',
                                      headers=self.user_create_token(),
                                      data=json.dumps(test_entry),
                                      content_type='application/json')
        return response

    def wrong_data(self):
        """Function to test trying make wrong entry"""
        self.create_an_entry()
        my_id = self.database.get_an_id()
        response = self.test_user.put('/api/v1/entries/{}'.format(my_id),
                                      headers=self.user_create_token(),
                                      data=json.dumps(wrong_test_entry),
                                      content_type='application/json')
        return response

    def helo(self):
        """Function to test hello world"""
        response = self.test_user.get('/', content_type="application/json")
        return response

    def error_page(self):
        """Function to test 404 errors"""
        response = self.test_user.get('/3/', content_type="application/json")
        return response

    def profile(self):
        """Function to test retruning profile"""
        response = self.test_user.get('/api/v1/profile',
                                      headers=self.user_create_token(),
                                      content_type='application/json')
        return response

    def edit_profession(self):
        """Function to test edit profile profession"""
        response = self.test_user.put('/api/v1/profile',
                                      headers=self.user_create_token(),
                                      data=json.dumps({'profession': 'Simon'}),
                                      content_type='application/json')
        return response

    def edit(self):
        """Function to test no parameter sent to edit profile"""
        response = self.test_user.put('/api/v1/profile',
                                      headers=self.user_create_token(),
                                      content_type='application/json')
        return response

    def pic_upload(self):
        """Function to test add pic"""
        data = {}
        data['photo'] = (io.BytesIO(b'test'), 'test_file.jpg')
        response = self.test_user.post('/api/v1/profile/pic',
                                       headers=self.user_create_token(),
                                       data=data,
                                       content_type='multipart/form-data')
        return response

    def pic_no_upload(self):
        """Function to test not add pic"""
        response = self.test_user.post('/api/v1/profile/pic',
                                       headers=self.user_create_token(),
                                       data=json.dumps({"path": ""}),
                                       content_type='application/json')
        return response

    def pic_not_added_upload(self):
        """Function to test add not pic"""
        data = {}
        response = self.test_user.post('/api/v1/profile/pic',
                                       headers=self.user_create_token(),
                                       data=data,
                                       content_type='multipart/form-data')
        return response
