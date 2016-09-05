import logging
from flask import request
from api.v1 import api_v1

logger = logging.getLogger(__name__)


@api_v1.app_errorhandler(422)
def handle_error(error):
    logger.info(u'Requested url = {} , arguments = {}'.format(request.url_rule, request.get_data()))
    key_list = list()
    for key in error.data['messages'].keys():
        key_list.append(key)
    rv = {
        'success': False,
        'error': {
            'code': 422,
            'error': u'Invalid value for the following keys {}'.format(key_list)
        },
        'errors': [u'Invalid value for the following keys {}'.format(key_list)]
    }
    res = jsonify(rv)
    res.status_code = 422
    return res
