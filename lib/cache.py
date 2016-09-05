import redis
import pickle
import logging

from config import REDISDB, REDISHOST, REDISPORT

rules_pool = redis.ConnectionPool(
    host=REDISHOST, port=REDISPORT, db=REDISDB)
cache_type = {
    'rules': rules_pool
}
logger = logging.getLogger(__name__)


def set(key, value, ctype='rules', ex=None, px=None, nx=False, xx=False):
    pool = cache_type.get(ctype)
    r = redis.StrictRedis(connection_pool=pool)
    return r.set(key, pickle.dumps(value), ex, px, nx, xx)


def get(key, ctype='rules'):
    pool = cache_type.get(ctype)
    r = redis.StrictRedis(connection_pool=pool)
    pickled_value = r.get(key)
    if pickled_value is None:
        return None
    result = pickle.loads(pickled_value)
    return result


def exists(key, ctype='rules'):
    pool = cache_type.get(ctype)
    r = redis.StrictRedis(connection_pool=pool)
    return r.exists(key)


def delete(key, ctype='rules'):
    pool = cache_type.get(ctype)
    r = redis.StrictRedis(connection_pool=pool)
    return r.delete(key)
