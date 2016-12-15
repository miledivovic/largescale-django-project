from django.shortcuts import get_object_or_404, render
from django.http import Http404, HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.conf.urls.static import static
from django.contrib.auth.decorators import login_required
import sys
import os.path
from models import Counter
import time


def counterToJson(counter):
    json = '{'

    milli = int(time.mktime(counter.timestamp.timetuple())*1000)
    json += '"date": '
    json += str(milli)
    json += ', '

    json += '"tag": '
    json += '"'
    json += counter.tag
    json += '"'
    json += ', '

    json += '"value": '
    json += str(counter.value)

    json += '}'
    return json


def dataToJson(counters):
    json = '{"HIHI": ['
    for c in counters:
        json += counterToJson(c)
        json += ','
    json = json[:-1]
    json += ']}'
    return json

@login_required
def data(request):
    latest_counter_list = Counter.objects.raw('SELECT timestamp, counter_id, tag, value FROM dashboard_counter;')
    context = {'latest_counter_list': latest_counter_list}
    return render(request, 'data.html', context)

@login_required
def dash(request):
    latest_counter_list = Counter.objects.raw('SELECT timestamp, counter_id, tag, value FROM dashboard_counter order by timestamp asc;')
    json = dataToJson(latest_counter_list)
    #print json
    return render(request, 'templates/dashboard.html', {"JSONdata" : json})


def index(request):
    return render(request, 'index.html')


