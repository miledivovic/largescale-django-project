from django.contrib import admin

from .models import Service
from .models import Node
from .models import Counter

# Register your models here.

admin.site.register(Service)
admin.site.register(Node)
admin.site.register(Counter)
