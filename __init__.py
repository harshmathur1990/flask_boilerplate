from flask import Flask
from lib import log
from src.models import FlaskDB
from api import api_v1


def create_app():
    app = Flask(__name__)
    log.setup_logging()
    FlaskDB.init()
    app.register_blueprint(api_v1)
    return app