#!/usr/bin/env python

import sys
import httplib
from time import sleep
from random import randint

urls = ['/one/', '/two/','/three/']

while True:
	url = urls[randint(0,2)]
	status = 0
	try:
	    #The actual HTTP request
	    conn = httplib.HTTPConnection('127.0.0.1', 8000, timeout=30)
	    conn.request("GET", url)
	    status = conn.getresponse().status
	except Exception, e:  
		print e
		status = -1
		
	# print url + " -> " + str(status)
	sleep(randint(0,2))	