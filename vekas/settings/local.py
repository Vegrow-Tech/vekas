from vekas.settings.base import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'vekas',
        'USER': 'keyurtalathi',
        'PASSWORD': 'password',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}