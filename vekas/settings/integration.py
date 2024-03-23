from vekas.settings.base import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'vekas_integration',
        'USER': 'admin',
        'PASSWORD': 'xsw2XSW@',
        'HOST': 'aurora-staging-instance-1.c2i3l4jtesco.ap-south-1.rds.amazonaws.com',
        'PORT': '3306',
    }
}