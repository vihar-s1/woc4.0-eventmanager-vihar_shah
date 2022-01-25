from django.db import models

# Create your models here.

class Event(models.Model):
    eventName = models.CharField(max_length=32)
    description = models.TextField()
    location = models.CharField(max_length=32)
    startDate = models.DateField(default=None)
    startTime = models.TimeField(default=None)
    endDate = models.DateField(default=None)
    endTime = models.TimeField(default=None)
    registerbyDate = models.DateField(default=None)
    registerbyTime = models.TimeField(default=None)
    hostEmail = models.EmailField(default=None)
    hostpwd = models.CharField(max_length=15)

    def __str__(self) -> str:
        return str(self.id) + " : " + self.eventName

class Participant(models.Model):
    name = models.CharField(max_length=20)
    contact = models.CharField(max_length=15)
    email = models.EmailField()
    event = models.ForeignKey(Event, on_delete=models.CASCADE, default=None)
    registerType = models.CharField(max_length=12, default=None)
    participantCount = models.IntegerField(default=1)

    def __str__(self) -> str:
        return str(self.id) + " : " + self.name  