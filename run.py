"""File to start the flask app"""
import os 

from flask import jsonify
from werkzeug.contrib.profiler import ProfilerMiddleware
import click
from main import create_app
from app.utils.fixtures import seed_database, create_tables
from dotenv import load_dotenv
load_dotenv()

app = create_app(os.environ.get('FLASK_ENV'))
app.wsgi_app = ProfilerMiddleware(app.wsgi_app, restrictions=[30])


@app.cli.command(context_settings=dict(token_normalize_func=str.lower))
def migrate():
    create_tables()


@app.cli.command(context_settings=dict(token_normalize_func=str.lower))
def seed():
    seed_database()


if __name__ == "__main__":
    app.run()
