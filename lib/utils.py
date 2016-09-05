import requests
import logging
import time
from flask import request
from dateutil import parser

logger = logging.getLogger(__name__)


def is_timezone_aware(datetime_obj):
    if datetime_obj.tzinfo is not None and datetime_obj.tzinfo.utcoffset(datetime_obj) is not None:
        return True
    return False


def get_intersection_of_lists(list1, list2, key=None):
    if not key:
        return [l for l in list1 if l in list2]
    else:
        return [l[key] for l in list1 if l in list2]


def make_api_call(url, method='GET', body=None, headers=dict(), params=dict()):
    # body must be a json serializable dict
    start = time.time()
    if method == 'GET':
        response = requests.get(url=url, headers=headers, params=params)
    elif method == 'POST':
        response = requests.post(url=url, headers=headers, json=body, params=params)
    elif method == 'PUT':
        response = requests.post(url=url, headers=headers, json=body, params=params)
    else:
        raise Exception(u'Method {} not supported'.format(method))
    logger.info(u'Url: {}, method: {}, headers: {}, Request Body: {} Status Code: {} Response Body: {} Total Time Taken: {}'.format(
            url, method, headers, body, response.status_code, response.text, time.time() - start))
    return response


def create_success_response(data):
    rv = {
        'success': True,
        'data': data
    }
    return rv


def create_error_response(error_code, code=500, error_msg='', error_list=[]): # error_list[ {'code': -1, 'error_msg': 'item detail not found'}]
    rv = {
        'success': False,
        'code': code,
        'error': {
            'code': error_code,
            'error_msg': error_msg,
            'error_list': error_list
        }
    }
    return rv


def unauthenticated():
    return create_error_response(401, u'Unauthenticated Client')


def get_agent_id():
    agent_id = None
    try:
        agent_id = request.user.agent_id
    except AttributeError:
        pass
    return agent_id


def date_validator(value):
    success = False
    try:
        parser.parse(value)
        success = True
    except:
        pass
    return success

def is_logged_in():
    # TODO: implement this if required
    return True
