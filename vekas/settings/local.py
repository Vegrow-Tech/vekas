from vekas.settings.base import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'vekas',
        'USER': 'local_user',
        'PASSWORD': 'm@1234',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}