from flask import Flask,jsonify,make_response,request

#example entries
entries=[]
app=Flask(__name__)


@app.route('/')
def index():
    return jsonify({'hello': 'world'}),200

    
@app.route('/api/v1/entries', methods=['GET'])
def get_all_entries():
    if request.method=="GET":
        return make_response(jsonify({'entries':entries})),200

@app.route('/api/v1/entries', methods=['POST'])
def make_new_entry():
    if request.method=="POST":
        data=request.json
        new_entry = {
            'entry_id':len(entries) + 1,
            'entry_date': data['entry_date'],
            'entry_name': data['entry_name'],
            'entry_content':data['entry_content']
        }
        entries.append(new_entry)
        return make_response(jsonify({'Message':new_entry})),201

@app.route('/api/v1/entries/<int:entry_no>', methods=['GET'])
def single_entry(entry_no):
    if request.method=='GET':
        resultlist = [d for d in entries if d.get('entry_id', '') == entry_no]
        if resultlist:
            return make_response(jsonify({'entries':resultlist[0]})),200 
        else:
            return make_response(jsonify({'result':'not found'})),404


@app.route('/api/v1/entries/<int:entry_no>', methods=['PUT'])
def edit_an_entry_(entry_no):
    if request.method=="PUT":
        data=request.json
        update = {
            'entry_id':len(entries) + 1,
            'entry_date': data['entry_date'],
            'entry_name': data['entry_name'],
            'entry_content':data['entry_content']
        }
        result = [entry for entry in entries if entry['entry_id'] == entry_no]
        if result:
            result[0]['entry_name'] = update['entry_id']
            result[0]['entry_content'] = update['entry_content']  
            return make_response(jsonify({"Entry updated":"PUT request"})), 201
        else:
            return make_response(jsonify({"Update Failed":"ERRor"})),401