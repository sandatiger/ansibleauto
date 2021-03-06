import os.path

DEBUG = True
DEV_ENV = True
PROD_ENV = False
#email configuration
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.163.com'  #to use gmail
EMAIL_HOST_USER = 'sanda_tiger@163.com'
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
EMAIL_HOST_PASSWORD = 'Sanda15921331583'
EMAIL_PORT = 25
ALLOWED_HOSTS = ['*']
#site infos
SITE_NAME = 'Dev_pro'


#project directories
PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__).decode('utf-8')).replace('\\', '/')
MEDIA_ROOT = os.path.join(PROJECT_ROOT, "media")
STATIC_ROOT = os.path.join(PROJECT_ROOT, "static_root")
TEMPLATE_ROOT = os.path.join(PROJECT_ROOT, "templates")
# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = '/media/'
ADMIN_MEDIA_PREFIX = '/media/admin/'
# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = '/static/'

ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)

MANAGERS = ADMINS

#DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.postgresql_psycopg2', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
#        'NAME': 'demo', # Or path to database file if using sqlite3.
#        'USER': 'postgres', # Not used with sqlite3.
#        'PASSWORD': '', # Not used with sqlite3.
#        'HOST': '127.0.0.1', # Set to empty string for localhost. Not used with sqlite3.
#        'PORT': '5432', # Set to empty string for default. Not used with sqlite3.
#    }
#}

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'demo', # Or path to database file if using sqlite3.
        'USER': 'root', # Not used with sqlite3.
        'PASSWORD': 'liuyin1986', # Not used with sqlite3.
        'HOST': '', # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '3306', # Set to empty string for default. Not used with sqlite3.
    }
}



CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://127.0.0.1:6379/10",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    }
}

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'secret'

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}
