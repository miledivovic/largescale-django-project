# -*- coding: utf-8 -*-
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world!")


def one(request):
    return HttpResponse("Hello, world one!")

def two(request):
    return HttpResponse("Hello, world two!")

def three(request):
    return HttpResponse("Hello, world three!")
