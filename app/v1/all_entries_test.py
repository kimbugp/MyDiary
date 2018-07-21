import unittest
import json
from app.v1 import app

class all_entries_test(unittest.TestCase):
    def create_app(self):
        app.config['TESTING'] = True
        return app
    #test if all entries are displayed
    def test_get_all_entries(self):
        """Tests that all entries can be retrieved"""
        testing_user = app.test_client(self)
        response = testing_user.get("/entries", content_type="application/json")
        assert b'1' in response.data
        assert b'3' in response.data

if __name__ == '__main__':
    unittest.main()
