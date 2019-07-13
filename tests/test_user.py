"""Module to test login/signup user activity """
import unittest

from tests.helpers import Helpers
from tests.base import TestingClass


class UserTests(TestingClass, Helpers):
    """Class to test endpoints"""

    def test_user_signup(self):
        """Method to test signup"""
        response = self.user_create()
        self.assertEqual(response.status_code, 201)
        self.assertIn('User created', str(response.data))

    def test_user_signup_wrong(self):
        """Method to test wrong signup"""
        response = self.wrong_user()
        self.assertEqual(response.status_code, 400)

    def test_user_already_exists(self):
        """Method to test existing user"""
        self.user_create()
        response = self.user_create()
        self.assertEqual(response.status_code, 400)
        self.assertIn('User already exists', str(response.data))

    def test_can_login_user(self):
        """Method to test signin"""
        response = self.user()
        self.assertEqual(response.status_code, 200)

    def test_create_user_with_invalid_email(self):
        response = self.wrong_user()
        self.assertEqual(response.status_code, 400)

    def test_user_login_with_no_info(self):
        """Method to test sign in with missing parameter"""
        response = self.wrong_details()
        self.assertIn(response.json['error'],
                      "'password' is a required property")

    def test_wrong_user_login(self):
        """Method to test sign in with wrong detail"""
        response = self.wrong_sign_in()
        self.assertEqual(response.status_code, 401)
        self.assertIn('Invalid login', str(response.data))

    def test_hello_world(self):
        """Method to test hello world"""
        response = self.helo()
        self.assertIn('hello', str(response.data))
        self.assertEqual(response.status_code, 200)

    def test_edit_profession(self):
        """Method to test editing profession"""
        response = self.edit_profession()
        self.assertEqual(response.status_code, 200)
