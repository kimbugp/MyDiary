"""File to start the flask app"""
from flask import jsonify

from app import app
from dotenv import load_dotenv
load_dotenv()

if __name__ == "__main__":
    app.run()
