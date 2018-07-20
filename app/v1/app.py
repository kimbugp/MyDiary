from flask import Flask,jsonify
from v1 import app
#example entries
entries=[
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

@app.route('/')
def index():
    return "Hello, World!"

@app.route('/entries', methods=['GET'])
def get_all_entries():
    return jsonify({'entries':entries}),200
