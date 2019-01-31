from django.conf.urls import include, url
from django.conf import settings
from local_settings import *
from django.views.static import serve

# Routers provide an easy way of automatically determining the URL conf.
# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.

from django.views.generic import TemplateView

urlpatterns = [

    #static
#    url(r'^static/(?P<path>.*)$',serve,
#            {'document_root': settings.STATIC_ROOT}),
    url(r'^static/(?P<path>.*)$',serve,
            {'document_root': '/usr/local/django/demo-app/ansible_demo/root_demo/static_root'}),

    #media
    url(r'^media/(?P<path>.*)$',serve,
            {'document_root': settings.MEDIA_ROOT}),

    #templates
#    url(r'^templates/(?P<path>.*)$',serve,
#            {'document_root': settings.TEMPLATE_ROOT}),
    url(r'^templates/(?P<path>.*)$',serve,
            {'document_root': '/usr/local/django/demo-app/ansible_demo/root_demo/templates'}),


    url(r'^demo_1/', include('demo_1.urls',
                            namespace='demo_1')),

]
