from django.db import models

# Create your models here.

class Event(models.Model):
    eventName = models.CharField(max_length=32)
    description = models.TextField()
    location = models.CharField(max_length=32)
    startDate = models.DateTimeField()
    endDate = models.DateTimeField()
    registerby = models.DateTimeField()
    hostEmail = models.EmailField()
    hostpwd = models.CharField(max_length=15)
    
    def __str__(self) -> str:
        return self.eventName + " organized by " + self.hostEmail

class Participant(models.Model):
    name = models.CharField(max_length=20)
    contact = models.CharField(max_length=15)
    email = models.EmailField()
    #event = models.ForeignKey(Event)

    