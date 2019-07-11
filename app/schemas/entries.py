import datetime

from jsonschema import validate

from app.utils.error_handlers import ValidationError

entries_schema = {
    'type': 'object',
    'properties': {
        'entry_name':  {"allOf": [
            {"type": "string"},
            {"minLength": 5}
        ]},
        'entry_content': {"allOf": [
            {"type": "string"},
            {"minLength": 5}
        ]},
    },
    'required': ['entry_name', 'entry_content']
}


def process_entry_json(var, partial=False):
    ''' Function to process json recieved from browser'''
    schema = entries_schema.copy()
    if partial:
        schema.pop('required')
    validate(var, schema)
    now = datetime.datetime.now()
    var['entry_date'] = now.strftime("%Y-%m-%d %H:%M")
    return var
