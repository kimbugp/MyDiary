from flask import jsonify, make_response
from jsonschema import ValidationError as Error

from app import app
from app.utils.error_handlers import ValidationError


@app.route('/')
def index():
    """
    End Point for the index page
    """
    return jsonify({'hello': 'world'}), 200


@app.errorhandler(404)
def page_not_found(e):
    """
    End Point to catch 404s
    """
    return make_response(jsonify({'message': 'Page not found'})), 404


@app.errorhandler(ValidationError)
def handle_invalid_usage(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response


@app.errorhandler(Error)
def handle_invalid_input(error):
    response = jsonify({'error': error.message})
    response.status_code = 400
    return response
