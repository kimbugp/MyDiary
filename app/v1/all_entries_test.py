import unittest
import json
from v1 import app

class all_entries_test(unittest.TestCase):
    def create_app(self):
        app.config['TESTING'] = True
        return app
    #test if all entries are displayed
    def display_all_entries(self):
        test = app.test_client(self)
        response = test.get("/entries", content_type="application/json")
        assert b'1' in response.data
        assert b'3' in response.data