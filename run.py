"""File to start the flask app"""
import os
from api import app
os.environ['app_env'] ='production'

if __name__ == '__main__':
    app.run(debug=True)
