"""Module to test API"""
from tests.base import TestingClass
from tests.helpers import Helpers


class TestEntriesModule(TestingClass, Helpers):
    """Class to test entries"""

    def test_get_all_entries(self):
        """Method to test getting all entry"""
        self.create_an_entry()
        response = self.get_an_entry()
        self.assertEqual(response.status_code, 200)
        self.assertIn("Test content", str(response.data))

    def test_making_a_new_entry(self):
        """Method to test making an entry"""
        response = self.create_an_entry()
        self.assertEqual(response.status_code, 201)
        self.assertIn("entry created", str(response.data))

    def test_mising_signup_parameter(self):
        """Method to test missing signup parameter"""
        response = self.create_wrong_entry()
        self.assertEqual(response.status_code, 400)

    def test_getting_single_entry(self):
        """Method to test getting single entry"""
        self.create_an_entry()
        response = self.get_single_entry()
        self.assertEqual(response.status_code, 200)
        self.assertIn("Test content", str(response.data))

    def test_getting_non_existing_entry(self):
        """Method to test non existing entry"""
        response = self.no_existing_entry()
        self.assertEqual(response.status_code, 404)
        self.assertIn("no entry", str(response.data))

    def test_editing_an_entry(self):
        """Method to test editing an entry"""
        response = self.edit_entry()
        self.assertEqual(response.status_code, 200)
        self.assertIn("entry edited", str(response.data))

    def test_missing_parameter(self):
        """Method to test missing parameter"""
        response = self.wrong_data()
        self.assertEqual(response.status_code, 400)

    def test_deleting_an_entry(self):
        """Method to test delelting entry"""
        response = self.delete_entry()
        self.assertEqual(response.status_code, 200)
        self.assertIn("successfully deleted", str(response.data))

    def test_user_working_with_no_token(self):
        """Method to test working with no token"""
        response = self.no_token()
        self.assertEqual(response.status_code, 401)
        self.assertIn("No auth token", str(response.data))

    def test_user_with_wrong_token(self):
        """Method to test working wrong token"""
        response = self.wrong_token()
        self.assertEqual(response.status_code, 401)
        self.assertIn("Invalid token", str(response.data))

    def test_editing_non_existing_entry(self):
        """Method to test editing non exisitng entry"""
        response = self.edit_no_entry()
        self.assertEqual(response.status_code, 404)
        self.assertIn("no such entry", str(response.data))

    def test_catching_general_404(self):
        """Method to test genral 404"""
        response = self.error_page()
        self.assertEqual(response.status_code, 404)

    def test_view_profile(self):
        """Method to test viewing user profile"""
        response = self.profile()
        self.assertEqual(response.status_code, 200)
