"""File to start the flask app"""
from flask import jsonify

from app import app
from app.utils.error_handlers import ValidationError


@app.errorhandler(ValidationError)
def handle_invalid_usage(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response

if __name__ == "__main__":
    app.run(load_dotenv=True)
