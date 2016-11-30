from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Service(models.Model):
     service_id = models.AutoField(primary_key=True)
     name = models.CharField(max_length=200)
     created = models.DateTimeField('date created')
     owner = models.ForeignKey(User, on_delete=models.CASCADE)
     active = models.BooleanField(default=True)

class Node(models.Model):
     node_id = models.AutoField(primary_key=True)
     service_id = models.ForeignKey(Service, on_delete=models.CASCADE)
     node_ip = models.CharField(max_length=25)
     probing_frequency = models.PositiveIntegerField()
     created = models.DateTimeField('date created')
     owner = models.ForeignKey(User, on_delete=models.CASCADE)
     last_probed = models.DateTimeField('last probed')
     active = models.BooleanField(default=True)
     error_msg = models.CharField(max_length=200)
     last_failure = models.DateTimeField('last failed')

class Counter(models.Model):
     counter_id = models.AutoField(primary_key=True)
     node_id = models.ForeignKey(Node, on_delete=models.CASCADE)
     timestamp = models.DateTimeField('date probed')
     tag = models.CharField(max_length=200)
     value = models.PositiveIntegerField()

