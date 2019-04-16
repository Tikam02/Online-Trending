import os
import django
from django.conf import settings
import pytest

# We manually designate which settings we will be using in an environment variable
# This is similar to what occurs in the `manage.py`
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'apex.settings.base')
@pytest.fixture(scope='session')
def django_db_setup():
    settings.DATABASES['default'] = {
        'ENGINE': 'django.db.backends.sqlite3',
        'HOST': 'http://127.0.0.1:8000/',
        'NAME': 'db.sqlite3',
    }
