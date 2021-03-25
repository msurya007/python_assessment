import os
from app import create_app
config_name = os.getenv('FLASK_CONFIG')
app = create_app(config_name)
if __name__ == '__main__':
    app.run()

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import app_config
db = SQLAlchemy()

def create_app(config_name):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')
    db.init_app(app)

    return app