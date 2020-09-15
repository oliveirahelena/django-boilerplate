from .base import *

DEBUG = True
ALLOWED_HOSTS += ['127.0.0.1', 'localhost']
WSGI_APPLICATION = 'demo.wsgi.dev.application'

DATABASES = {
    'default': env.db('SQLITE_URL', default='sqlite:///db.sqlite3')
}

# E-mail
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
