from django.contrib import admin
from event_manager_app.models import *

#from django.contrib.admin.models import LogEntry
#LogEntry.objects.all().delete()

# Register your models here.
admin.site.register(Event)
admin.site.register(Participant)