"""Module to test login/signup user activity """
import unittest

from tests.base import (TestingClass, edit, edit_profession, helo,
                        pic_no_upload, pic_not_added_upload, pic_upload, user,
                        user_create, wrong_details, wrong_sign_in, wrong_user)


class UserTests(TestingClass):
    """Class to test endpoints"""

    def test_user_signup(self):
        """Method to test signup"""
        response = user_create(self.test_user)
        self.assertEqual(response.status_code, 201)
        self.assertIn('User created', str(response.data))

    def test_user_signup_wrong(self):
        """Method to test wrong signup"""
        response = wrong_user(self.test_user)
        self.assertEqual(response.status_code, 400)
        self.assertIn('parameter missing', str(response.data))

    def test_user_already_exists(self):
        """Method to test existing user"""
        user_create(self.test_user)
        response = user_create(self.test_user)
        self.assertEqual(response.status_code, 400)
        self.assertIn('User already exists', str(response.data))

    def test_can_login_user(self):
        """Method to test signin"""
        response = user(self.test_user)
        self.assertEqual(response.status_code, 200)

    def test_user_login_with_no_info(self):
        """Method to test sign in with missing parameter"""
        response = wrong_details(self.test_user)
        self.assertIn('parameter missing', str(response.data))

    def test_wrong_user_login(self):
        """Method to test sign in with wrong detail"""
        response = wrong_sign_in(self.test_user)
        self.assertEqual(response.status_code, 401)
        self.assertIn('Invalid login', str(response.data))

    def test_hello_world(self):
        """Method to test hello world"""
        response = helo(self.test_user)
        self.assertIn('hello', str(response.data))
        self.assertEqual(response.status_code, 200)
    
    def test_edit_profession(self):
        """Method to test editing profession"""
        response=edit_profession(self.test_user)
        self.assertEqual(response.status_code,200)
    
    def test_edit_profile(self):
        """Method to test editing profile"""
        response=edit(self.test_user)
        self.assertEqual(response.status_code,400)
    
    def test_add_pic(self):
        """Method to test adding profilepic"""
        response=pic_upload(self.test_user)
        self.assertEqual(response.status_code,201)

    def test_not_add_pic(self):
        """Method to test not adding profilepic"""
        response=pic_no_upload(self.test_user)
        self.assertEqual(response.status_code,400)
    
    def test_added_pic_invalid(self):
        """Method to test not adding profilepic"""
        response=pic_not_added_upload(self.test_user)
        self.assertEqual(response.status_code,400)



if __name__ == '__main__':
    unittest.main()
