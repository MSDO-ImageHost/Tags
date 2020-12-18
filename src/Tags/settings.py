import os

from pathlib import Path


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Environment variables
try:
    AMQP_USER = os.environ["AMQP_USER"]
    AMQP_PASS = os.environ["AMQP_PASS"]
    AMQP_HOST = "rabbitmq"
    MYSQL_USER = os.environ["MYSQL_USER"]
    MYSQL_PASS = os.environ["MYSQL_PASS"]
    MYSQL_HOST = os.environ["MYSQL_HOST"]
    SECRET_KEY = os.environ["SECRET_KEY"]
except KeyError:
    AMQP_USER = "guest"
    AMQP_PASS = "guest"
    AMQP_HOST = "localhost"
    MYSQL_USER = "root"
    MYSQL_PASS = ""
    MYSQL_HOST = "localhost"
    SECRET_KEY = "secret"

# Application definition
INSTALLED_APPS = [
    'api.apps.ApiConfig',
    'django_extensions'
]


# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': "Tags",
        'USER': MYSQL_USER,
        'PASSWORD': MYSQL_PASS,
        'HOST': MYSQL_HOST,
        'PORT': 3306
    }
}


# Internationalization
LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True
