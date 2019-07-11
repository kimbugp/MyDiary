"""File to start the flask app"""
from flask import jsonify

from app import app


if __name__ == "__main__":
    app.run(load_dotenv=True)
