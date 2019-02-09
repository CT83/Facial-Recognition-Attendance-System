import django_heroku
from django.db import connection

# noinspection PyUnresolvedReferences
from .base import *

DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'un&w%=62vsnnzl4xrc$%vj8-0ex4p(q1afn%za1j=1teb(i_5='

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = ['*']

print("Using Production Settings...")
try:
    from .local import *
except ImportError:
    pass

django_heroku.settings(locals())

db_name = connection.settings_dict['NAME']
print("Using Database:", db_name)
