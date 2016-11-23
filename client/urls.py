from django.conf.urls import include, url
from . import counter

urlpatterns = [
    url(r'^counters/$', counter.getData, name='counters'),
]
