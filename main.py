from config import app_config
from flask import Flask
from app.models.models import MODELS
from flask_cors import CORS


def create_app(config):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(app_config.get(config))
    app.url_map.strict_slashes = False
    
    # add cors
    CORS(app)
    # bind app to db
    db = MODELS()
    db.create_user_table()
    db.create_entries_table()

    return app
