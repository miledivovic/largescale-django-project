import json
from django.http import JsonResponse

#Dictionary containing all counters by tag
counters = {}

#Increments the counters by specified tag
def increment(tag):
	#If the tag exists, increment its value
	if counters.has_key(tag):
		counters[tag] = counters[tag] + 1
	#Otherwise, create the key for the tag and set it to 1
	else:
		counters[tag] = 1
	#Optionally print out the counters and their values
	#printCounters()

#Print out the counters by tag and value
def printCounters():
	print "---------"
	for key in counters:
		print key + ": " + str(counters[key])
	print "---------"

#Function for returning the JSON HTTP Response of all the counters
#Used in urls.py
def getData(request):
  return JsonResponse(counters)