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
print PROJECT_ROOT
print MEDIA_ROOT
print STATIC_ROOT
print TEMPLATE_ROOT
