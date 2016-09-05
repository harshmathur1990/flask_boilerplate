from flask import Blueprint

api_v1 = Blueprint('v1', __name__, url_prefix='/api/v1')
import api, errors