from django.conf.urls import include, url
from . import counter

#For the URL of the page returns the JSON of counters
urlpatterns = [
    url(r'^counters/$', counter.getData, name='counters'),
]
