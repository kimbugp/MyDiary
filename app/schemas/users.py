import re

from jsonschema import validate

from app.utils.error_handlers import ValidationError

user_schema = {
    'type': 'object',
    'properties': {
        'username':  {"allOf": [
            {"type": "string"},
            {"minLength": 5}
        ]},
        'email': {"allOf": [
            {"type": "string"},
            {"minLength": 5},
            {'format': 'email'},
        ]},
        'password': {"allOf": [
            {"type": "string"},
            {"minLength": 5}
        ]},
        'name': {"allOf": [
            {"type": "string"},
            {"minLength": 5}
        ]},
    },
    'required': ['username', 'email', 'password', 'name']
}

user_login_schema = {
    'type': 'object',
    'properties': {
        'username':  {"allOf": [
            {"type": "string"},
            {"minLength": 5}
        ]},
        'password': {"allOf": [
            {"type": "string"},
            {"minLength": 5}
        ]},
    },
    'required': ['username', 'password']
}


def process_user_json(var, partial=False):
    ''' Function to process user signup info from browser'''
    schema = user_schema.copy()
    if partial:
        schema.pop('required')
    validate(var, schema)
    if re.match(r'\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}\b', var['email'], re.I) and re.match("^[A-Za-z0-9_-]*$", var['username']):
        return var
    raise ValidationError('error', payload={'message': 'provide a valid email and username'})



def process_signin_json(var):
    ''' Function to process user login info from browser'''
    schema = user_login_schema.copy()
    validate(var, schema)
