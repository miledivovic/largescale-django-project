# -*- coding: utf-8 -*-

from django.conf.urls import patterns, include
from django.conf import settings
from djanitor import urls

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^helloworld/', include('helloworld.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),

    # Hello, world!
    # (r'', 'helloworld.views.index'),

    (r'^one/', 'demo.views.one'),

    (r'^two/', 'demo.views.two'),

    (r'^three/', 'demo.views.three'),

    url(r'^djanitor/', include('djanitor.urls', namespace="djanitor"))
)

if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve',
         {'document_root': settings.MEDIA_ROOT}),
    )

