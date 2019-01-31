import os.path
import posixpath
from local_settings import *
TEMPLATE_DIRS = (
    TEMPLATE_ROOT,
    os.path.join(os.path.dirname(__file__), 'templates').replace('\\','/'),
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

print TEMPLATE_DIRS
