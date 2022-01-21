from traceback import print_tb
from django.shortcuts import render
from event_manager_app.models import *

# Create your views here.
def index(request):
    context = {
        'message' : 'site under construction!'
    }
    return render(request, 'index.html',context)

def organize(request):
    context = {}
    return render(request, 'organizeEvent.html', context)

def newEventRequest(request):
    context = {}
    new_event = Event()
    new_event.eventName = request.POST['event_name']
    new_event.description = request.POST['description']
    new_event.location = request.POST['location']
    new_event.startDate = request.POST['startDate']
    new_event.startTime = request.POST['startTime']
    new_event.endDate = request.POST['endDate']
    new_event.endTime = request.POST['endTime']
    new_event.registerbyDate = request.POST['registerByDate']
    new_event.registerbyTime = request.POST['registerByTime']
    new_event.hostEmail = request.POST['hostEmail']
    new_event.hostpwd = request.POST['hostPwd']

    new_event.save()

    return render(request, 'organizeEvent.html', context)

def register(request):
    try:
        events = Event.objects.all()
        if len(events) == 0: events = None
    except:
        events = None

    context = { 'Events' : events }
    return render(request, 'registerEvent.html', context)

def dashboard(request):
    context = {}
    return render(request, 'dashboard.html', context)

