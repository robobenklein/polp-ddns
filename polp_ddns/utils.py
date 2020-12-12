
import datetime
import pytz
import urllib

from flask import make_response

def escape_url(url):
    return urllib.parse.quote_plus(url)

def get_datetime_now_aware():
    return datetime.datetime.now(pytz.utc)

def force_nocache_response(response):
    response.cache_control.max_age = 0
    response.cache_control.no_cache = True
    response.cache_control.no_store = True
    response.cache_control.must_revalidate = True
