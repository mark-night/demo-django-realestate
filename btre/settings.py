import os
import sys


ENVS = ['SECRET_KEY', 'DB_HOST', 'DB_NAME', 'DB_USER', 'DB_PASSWORD']
ENV_MISSING = False
for key in ENVS:
    if key not in os.environ:
        print(f'{key} is needed but not set.')
        ENV_MISSING = True
if ENV_MISSING:
    sys.exit('Some environment variables are missing. Aborted.')

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ['SECRET_KEY']


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
ALLOWED_HOSTS = []
if 'DEBUG_MODE' in os.environ and os.environ['DEBUG_MODE'].lower() == 'false':
    if 'ALLOWED_HOSTS' not in os.environ:
        sys.exit('ALLOWED_HOSTS must be set in production. Aborted.')
    DEBUG = False
    ALLOWED_HOSTS = os.environ['ALLOWED_HOSTS'].split(' ')


# Application definition

INSTALLED_APPS = [
    'apps.pages.apps.PagesConfig',
    'apps.listings.apps.ListingsConfig',
    'apps.realtors.apps.RealtorsConfig',
    'apps.accounts.apps.AccountsConfig',
    'apps.contacts.apps.ContactsConfig',
    'django.contrib.humanize',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'btre.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        # ! where else to look for 'templates'
        'DIRS': [os.path.join(BASE_DIR, 'btre/templates')],
        # ! if installed apps have their own 'templates' dir
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'btre.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.environ['DB_NAME'],
        'USER': os.environ['DB_USER'],
        'PASSWORD': os.environ['DB_PASSWORD'],
        'HOST': os.environ['DB_HOST'],
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'btre/static')
]
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# FORCE_SCRIPT_NAME is only supported in Django >= 3.1
scriptname = '' if 'BASE_URL' not in os.environ else os.environ['BASE_URL']
STATIC_URL = scriptname + '/static/'
MEDIA_URL = scriptname + '/media/'
