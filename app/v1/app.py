from flask import Flask,jsonify,make_response,request
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
app=Flask(__name__)

def search(entry_id):
    for p in entries:
        if p['entry_id'] ==entry_id:
            return p

@app.route('/')
def index():
    return "Hello, World!"

@app.route('/entries', methods=['GET','POST'])
def get_all_entries():
    if request.method=="GET":
        return jsonify({'entries':entries}),200
    elif request.method=="POST":
        return make_response(jsonify({'result':'posted'})),201

@app.route('/entries/<entry_no>', methods=['GET','PUT'])
def single_entry(entry_no):
    if request.method=='GET':
        resultlist = [d for d in entries if d.get('entry_id', '') == entry_no]
        if resultlist:
            return make_response(jsonify({'entries':resultlist[0]})),200 
        else:
            return make_response(jsonify({'result':'not found'})),404

    elif request.method=='PUT':
        return make_response(jsonify({'result':'edited'})),201
        