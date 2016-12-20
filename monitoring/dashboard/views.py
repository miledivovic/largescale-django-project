from django.shortcuts import get_object_or_404, render
from django.http import Http404, HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.conf.urls.static import static
from django.contrib.auth.decorators import login_required
import sys
import os.path
from models import Counter
import time


def counterToJson(counter, subtract):
    json = '{'

    milli = int(time.mktime(str(counter.d+" "+counter.h+":00:00").timetuple())*1000)
    json += '"date": '
    json += str(milli)
    json += ', '

    json += '"tag": '
    json += '"'
    json += counter.tag
    json += '"'
    json += ', '

    json += '"value": '
    json += str(counter.v - subtract)

    json += '}'
    return json


def dataToJson(counters):
    json = '{"HIHI": ['
    dic = {}
    for c in counters:
        previous_value = 0
        if c.tag in dic:
            previous_value = dic[c.tag]
            dic[c.tag] = c.v
        json += counterToJson(c, previous_value)
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
    latest_counter_list = Counter.objects.raw("SELECT date(timestamp) as d , hour(timestamp) as h, tag, SUM(value) as v, max(counter_id) FROM dashboard_counter WHERE counter_id <> 0 GROUP BY date(timestamp),  hour(timestamp), tag ORDER BY date(timestamp), hour(timestamp);")
    json = dataToJson(latest_counter_list)
    #print json
    return render(request, 'templates/dashboard.html', {"JSONdata" : json})

def index(request):
    return render(request, 'index.html')
