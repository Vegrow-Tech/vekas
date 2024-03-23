from datetime import datetime
from time import mktime
from django.utils import timezone

import pytz
import os
from flask import current_app as app


import random
import string


def generate_random_string(length=10):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choices(characters, k=length))


def get_utc_ms_time(date):
    try:
        return int(mktime(date.timetuple()))*1000

    except:
        return ''
    

def current_time():
    return datetime.now(pytz.timezone('Asia/Kolkata'))

def current_time_in_ms():
    return mktime(datetime.now().timetuple()) * 1000


def utc_to_local(utc_dt):
    return utc_dt.astimezone(
        tz=pytz.timezone('Asia/Kolkata'))  # .astimezone(tz=None)


def get_utc_ms_time(date):
    date = utc_to_local(date)
    try:
        return (int(mktime(date.utctimetuple())) * 1000)

    except Exception as e:
        return ''


def get_str_datetime(date):
    try:
        return date.strftime('%d %b %Y %H:%M')
    except Exception as e:
        return ''


def utc_ms_to_date(utc_ts):
    try:
        date_obj = datetime.fromtimestamp(float(utc_ts) / 1000.0).replace(
            tzinfo=pytz.timezone('Asia/Kolkata'))
    except Exception as e:
        date_obj = None
    return date_obj

def default_expiry_date():
    return timezone.now() + timezone.timedelta(days=30)