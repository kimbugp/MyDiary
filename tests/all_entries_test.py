import unittest
from flask import Flask,jsonify,make_response,request
import sys
import json

from api import app
from api.v1.app import entries

''' Dummy Data'''
test_entry= {
                'entry_id':'1',
                'entry_date':'25/10/1995 20:15',
                'entry_name':'Dummy Entry',
                'entry_content':'Test Content'
            }
test_entry2= {
                'entry_id':'1',
                'entry_date':'25/10/1995 20:15',
                'entry_name':'Edited',
                'entry_content':'Edited'
            }
class all_entries_test(unittest.TestCase):
    def create_app(self):
        app.config['TESTING'] = True
        return app
    
    #test if all entries are displayed
    def test_get_all_entries(self):
        # Tests that all entries can be retrieved
        testing_user = app.test_client(self)
        response = testing_user.get("/api/v1/entries", content_type="application/json")
        self.assertEqual(response.status_code,200)

    def test_API_can_create_new_entries(self):
        test_user=app.test_client(self)
        response=test_user.post('/api/v1/entries',data=json.dumps(test_entry),content_type="application/json")
        self.assertIn('Test Content',str(response.data),msg="all entries valid")
        self.assertEqual(response.status_code,201)

    def test_API_get_one_entry(self):
        # Tests to show one  entry
        test_user = app.test_client(self)
        test_user.post('/api/v1/entries',data=json.dumps(test_entry),content_type="application/json")
        response = test_user.get('/api/v1/entries/1',data=json.dumps(test_entry),content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertIn('Test Content', str(response.data))
    
    def test_hello_world(self):
        testing_user = app.test_client(self)
        response =testing_user.get('/',content_type="application/json")
        # self.assertIn('hello',str(response.data))
        self.assertEqual(response.status_code,200)
    
    def test_edit_an_entry(self):
        # Tests to edit an entry
        testing_user = app.test_client(self)
        testing_user.post('/api/v1/entries', data=json.dumps(test_entry2),
                                    content_type='application/json')
        response = testing_user.put('/api/v1/entries/1', data=json.dumps(test_entry2),
                                    content_type='application/json')
        self.assertEqual(response.status_code, 201)
        
if __name__ == '__main__':
    unittest.main()
