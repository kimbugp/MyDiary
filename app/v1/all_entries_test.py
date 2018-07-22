import unittest
from flask import Flask,jsonify,make_response,request
import sys
import json

# Add a dummy Resource to verify that the app is properly set.
# class HelloWorld(flask_restful.Resource):
#     def get(self):
#         return {}

app=Flask(__name__)
class all_entries_test(unittest.TestCase):
    def create_app(self):
        app.config['TESTING'] = True
        return app
    
    def setup(self):
        self.entries=[
            {
                'entry_id':'1',
                'entry_date':'25/10/1995 20:15',
                'entry_name':'Dummy Entry',
                'entry_content':'Test Content'
            },
            {
                'entry_id':'2',
                'entry_date':'25/10/1995 20:15',
                'entry_name':'Dummy Entry',
                'entry_content':'Test Content'
            },
            {
                'entry_id':'3',
                'entry_date':'25/10/1995 20:15',
                'entry_name':'Dummy Entry',
                'entry_content':'Test Content'
            },
        ]

    #test if all entries are displayed
    def test_get_all_entries(self):
        # Tests that all entries can be retrieved
        testing_user = app.test_client(self)
        response = testing_user.get("/entries", content_type="application/json")
        assert b'1' in response.data
        assert b'3' in response.data
    
    def test_API_can_make_new_entry(self):
        # Tests for a new entry
        testing_user = app.test_client(self)
        response = testing_user.post('/entries', data=json.dumps(self.entries[0]),
                                     content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertIn(self.entries[0]['entry_name'], str(response.data),msg="No entry made")
    
    def test_hello_world(self):
        testing_user = app.test_client(self)
        response =testing_user.get('http://localhost:5000')
        self.assertEqual(response.json(), {'hello': 'world'})
        
if __name__ == '__main__':
    unittest.main()
