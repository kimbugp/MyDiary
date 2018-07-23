from flask import Flask,jsonify,make_response,request
# from v1 import app
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
    return {'hello': 'world'}

@app.route('/entries', methods=['GET','POST'])
def get_all_entries():
    if request.method=="GET":
        return jsonify({'entries':entries}),201

    elif request.method=="POST":
        # if not request.json or not 'entry_id' in request.json:
            # return make_response(jsonify({'result':'no data'})),200
        #test update dictionary
        new_entry ={
            'entry_id':'5',
            'entry_date':'25/10/1995 20:15',
            'entry_name':'Dummy Entry new',
            'entry_content':'Test Content2'
        }
        # new_entry= request.get_json()
        # new_entry = {
        #     'entry_id':len(entries) + 1,
        #     'entry_date': request.json.get('date',""),
        #     'entry_name': request.json.get('name', ""),
        #     'entry_content':request.json.get('content',"")
        # }
        entries.append(new_entry)
        return jsonify({'Message':new_entry}),200

@app.route('/entries/<entry_no>', methods=['GET','PUT'])
def single_entry(entry_no):
    if request.method=='GET':
        resultlist = [d for d in entries if d.get('entry_id', '') == entry_no]
        if resultlist:
            return make_response(jsonify({'entries':resultlist[0]})),200 
        else:
            return make_response(jsonify({'result':'not found'})),404

    elif request.method=='PUT':
        # update = request.get_json()
        # test update dictionary
        update ={
            'entry_id':'3',
            'entry_date':'25/10/1995 20:15',
            'entry_name':'Dummy Entry new',
            'entry_content':'Test Content2'
        }

        result = [entry for entry in entries if entry['entry_id'] == entry_no]
        if result:
            if 'entry_name' in update:
                result[0]['entry_name'] = update['entry_name']

            if 'entry_content' in update:
                result[0]['entry_content'] = update['entry_content']
                
            return make_response(jsonify({"Entry updated":"PUT request"})), 201
        else:
            return make_response(jsonify({"Update Failed":"ERRor"})), 200
        