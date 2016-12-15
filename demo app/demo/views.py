# -*- coding: utf-8 -*-
from django.http import HttpResponse
from djanitor import counter

def index(request):
	djanitor.increment("index")
    return HttpResponse("Hello, world!")


def one(request):
	djanitor.increment("one")
    return HttpResponse("Hello, world one!")

def two(request):
	djanitor.increment("two")
    return HttpResponse("Hello, world two!")

def three(request):
	djanitor.increment("three")
    return HttpResponse("Hello, world three!")
