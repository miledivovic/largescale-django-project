#Dictionary containing all tags
import json
from django.http import JsonResponse

counters = {}

def increment(tag):
	#If the counters dictionary already has the tag, increment its value
	if counters.has_key(tag):
		counters[tag] = counters[tag] + 1
	#Otherwise, create the key for the tag and set it to 1
	else:
		counters[tag] = 1
	toJSON()

def toJSON():
	result = ""
	for key in counters:
		print key + ": " + str(counters[key])
	print "---------"

def getData(request):
  return JsonResponse(counters)
