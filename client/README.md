How to use the client
------------------------------    


1) Creating & Incrementing Counters

	Import client into the script(s) that want to increment counters, using the following command:
		from monitoring import counter

	Then just call the following API, with the Counter Name that you want to increment:
		counter.increment(`COUNTER NAME`)

	The client will create a new counter with value 1 if it doesn't exist, else it will increment the existing value by 1

2) View to give Prober access to the data

	Do the following in the main website's urls.py

	Import monitoring url, using the following command:
		from monitoring import urls	

	Then added the following line in urlpatterns list:
		url(r'^monitoring/', include('monitoring.urls', namespace="monitoring"))



