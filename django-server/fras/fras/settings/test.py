import sys

from .base import *

TEST_NAME = "Unit_Test"

if 'test' in sys.argv:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(os.path.dirname(__file__), 'test.db'),
            'TEST_NAME': os.path.join(os.path.dirname(__file__), 'test.db'),
        }
    }
