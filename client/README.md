How to use the client
------------------------------
## Creating & Incrementing Counters

Import client into the script(s) that want to increment counters, using the following command:
```python
from monitoring import counter
```

Then just call the following API, with the counter tag that you want to increment:
```python
counter.increment('COUNTER NAME')
```

The client will create a new counter with value 1 if it doesn't exist. Otherwise, it will increment the existing value by 1.

## View to give Prober access to the data

Do the following in the main website's urls.py

Import monitoring url, using the following command:
```python
from monitoring import urls	
```

Then added the following line in urlpatterns list:
```python
url(r'^monitoring/', include('monitoring.urls', namespace="monitoring"))
```