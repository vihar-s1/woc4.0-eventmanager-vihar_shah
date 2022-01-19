from django.db import models

# Create your models here.

class Event(models.Model):
    eventName = models.CharField(max_length=32)
    description = models.TextField
    location = models.CharField(max_length=32)
    startFrom = models.DateTimeField
    endat = models.DateTimeField
    registerby = models.DateTimeField
    hostEmail = models.EmailField
    hostpwd = models.CharField(max_length=15)
    
    def __str__(self) -> str:
        return self.eventName + " organized by " + self.hostEmail