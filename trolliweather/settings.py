"""
Django settings for trolliweather project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'xsd!5@8$)b^f8sp5l3gja^k7ivp10d=dsyd7dz3ix52dfu3l$w'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'mongoadmin',
    'mongodbforms',
    'mongoengine.django.mongo_auth',
)



MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'trolliweather.urls'

WSGI_APPLICATION = 'trolliweather.wsgi.application'


MONGOADMIN_OVERRIDE_ADMIN = True

AUTHENTICATION_BACKENDS = ( 
           'mongoengine.django.auth.MongoEngineBackend',
 )
AUTH_USER_MODEL = 'mongo_auth.MongoUser'
MONGOENGINE_USER_DOCUMENT = 'mongoengine.django.auth.User'

SESSION_ENGINE = 'mongoengine.django.sessions'

# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.dummy',
#        'ENGINE': 'django.db.backends.sqlite3',
#        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

from mongoengine import connect
MONGO_DATABASE_NAME = 'testdb'
MONGO_HOST = '127.0.0.1'
MONGO_PORT = 27017
connect(MONGO_DATABASE_NAME, host=MONGO_HOST, port=MONGO_PORT)

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Europe/Paris'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'
