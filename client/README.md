How to use the client
------------------------------    

1) Import client using the following command:
      from monitoring import counter

2) Creating & Incrementing Counters
      counter.increment(`COUNTER NAME`)

  The client will create a new counter with value 1 if it doesn't exist, else it will increment the existing value by 1