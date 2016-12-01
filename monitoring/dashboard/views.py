from django.shortcuts import get_object_or_404, render
from django.http import Http404, HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.conf.urls.static import static
import sys
import os.path
from models import Counter

sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))
from settings import JSONFILES_FOLDER


def data(request):
    latest_counter_list = Counter.objects.order_by('-timestamp')
    context = {'latest_counter_list': latest_counter_list}
    return render(request, 'dashboard/data.html', context)


def dash(request):
	json_file = JSONFILES_FOLDER+"/data.json"
	f = open(json_file)
	d = f.readline()
	return render(request, 'templates/dashboard/dashboard.html', {"JSONdata" : d})


def config(request):
    return render(request, 'dashboard/config.html')

def index(request):
    return render(request, 'dashboard/index.html')


