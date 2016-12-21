from django.http import HttpResponse
from djanitor import counter

def one(request):
    counter.increment("one")
    return HttpResponse("Hello, world one!")

def two(request):
    counter.increment("two")
    return HttpResponse("Hello, world two!")

def three(request):
    counter.increment("three")
    counter.increment("2nd three")
    return HttpResponse("Hello, world three!")
