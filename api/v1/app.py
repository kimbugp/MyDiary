from flask import Flask,jsonify,make_response,request
from api import app

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
# app=Flask(__name__)


@app.route('/api/v1/')
def index():
    return jsonify({'hello': 'world'}),200

    
@app.route('/api/v1/entries', methods=['GET','POST'])
def get_all_entries():
    if request.method=="GET":
        return jsonify({'entries':entries}),200

    elif request.method=="POST":
        new_entry = {
            'entry_id':len(entries) + 1,
            'entry_date': request.form.get('date'),
            'entry_name': request.form.get('name'),
            'entry_content':request.form.get('content')
        }
        entries.append(new_entry)
        return jsonify({'Message':new_entry}),201

@app.route('/api/v1/entries/<entry_no>', methods=['GET','PUT'])
def single_entry(entry_no):
    if request.method=='GET':
        resultlist = [d for d in entries if d.get('entry_id', '') == entry_no]
        if resultlist:
            return make_response(jsonify({'entries':resultlist[0]})),200 
        else:
            return make_response(jsonify({'result':'not found'})),404

    elif request.method=='PUT':
        update = {
            'entry_id':entry_no,
            'entry_date': request.form.get('date'),
            'entry_name': request.form.get('name'),
            'entry_content':request.form.get('content')
        }

        result = [entry for entry in entries if entry['entry_id'] == entry_no]
        if result:
            if 'entry_name' in update:
                result[0]['entry_name'] = update['entry_id']

            if 'entry_content' in update:
                result[0]['entry_content'] = update['entry_content']
                
            return make_response(jsonify({"Entry updated":"PUT request"})), 201
        else:
            return make_response(jsonify({"Update Failed":"ERRor"})),401
            