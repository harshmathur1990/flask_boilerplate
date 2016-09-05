import json
import logging
from flask import request
import requests
from lib.decorator import jsonify, check_login
from lib.utils import is_timezone_aware, create_error_response,\
    create_success_response
    from webargs.flaskparser import parser, use_args
from api.v1 import api_v1
from api_args import args, update_awb_args
from datetime import datetime, timedelta
from dateutil import relativedelta, parser
from config import CONFIG
import decimal
import pytz
import copy
from lib import cache

logger = logging.getLogger(__name__)


@api_v1.route('/route', methods=['POST'])
@use_args(get_shipment_options_args)
@jsonify
def get_shipment_options(args):
    logger.info(u'Requested url = {} , arguments = {}'.format(request.url_rule, request.get_data()))
    return create_success_response(data)
