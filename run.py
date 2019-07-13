"""File to start the flask app"""
from flask import jsonify
import click
from app import app, db
from app.utils.fixtures import seed_database, create_tables
from dotenv import load_dotenv
load_dotenv()


@app.cli.command(context_settings=dict(token_normalize_func=str.lower))
def migrate():
    create_tables()


@app.cli.command(context_settings=dict(token_normalize_func=str.lower))
def seed():
    seed_database()


if __name__ == "__main__":
    app.run()
