import os

from pathlib import Path


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Environment variables
try:
    AMQP_USER = os.environ["RABBITMQ_USERNAME"]
    AMQP_PASS = os.environ["RABBITMQ_PASSWORD"]
    AMQP_HOST = os.environ["RABBITMQ_HOST"]
    MYSQL_USER = os.environ["MYSQL_USER"]
    MYSQL_PASS = os.environ["MYSQL_PASSWORD"]
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

print("MYSQL_HOST", MYSQL_HOST)


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
