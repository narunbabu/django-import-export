from __future__ import unicode_literals

import os

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',

    'import_export',

    'core',
]

SITE_ID = 1

ROOT_URLCONF = "urls"

DEBUG = True

STATIC_URL = '/static/'

SECRET_KEY = '2n6)=vnp8@bu0om9d05vwf7@=5vpn%)97-!d*t4zq1mku%0-@j'

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': (
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ),
        },
    },
]

if os.environ.get('IMPORT_EXPORT_TEST_TYPE') == 'mysql-innodb':
    IMPORT_EXPORT_USE_TRANSACTIONS = True
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'TEST_NAME': 'import_export_test',
            'USER': os.environ.get('IMPORT_EXPORT_MYSQL_USER', 'root'),
            'OPTIONS': {
               'init_command': 'SET storage_engine=INNODB',
            }
        }
    }
elif os.environ.get('IMPORT_EXPORT_TEST_TYPE') == 'postgres':
    IMPORT_EXPORT_USE_TRANSACTIONS = True
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'import_export',
            'USER': os.environ.get('IMPORT_EXPORT_POSTGRESQL_USER'),
            'PASSWORD': os.environ.get('IMPORT_EXPORT_POSTGRESQL_PASSWORD'),
            'HOST': 'localhost',
            'PORT': 5432
        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(os.path.dirname(__file__), 'database.db'),
        }
    }
    # DATABASES = {
    #     'default': {
    #         'ENGINE': 'django.db.backends.mysql', 
    #         'NAME': 'yourdbname',                      
    #         'USER': 'root',                      
    #         'PASSWORD': 'password',         
    #         'HOST': '127.0.0.1',                 
    #         'PORT': '3306',                      
    #     },
    # }
    # DATABASES = {
    #     'default': {
    #         'ENGINE': 'django.db.backends.mysql', 
    #         'NAME': 'DB_NAME',
    #         'USER': 'ab',
    #         'PASSWORD': '1',
    #         'HOST': 'localhost',   # Or an IP Address that your DB is hosted on
    #         'PORT': '3306',
    #     }
    # }

    

LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'handlers': {
        'console': {
            'class': 'logging.NullHandler'
        }
    },
    'root': {
        'handlers': ['console'],
    }}
