from django.shortcuts import render
from event_manager_app.models import *
from datetime import date, datetime, time

# Create your views here.
def index(request):
    context = {}
    return render(request, 'index.html',context)

def organize(request):
    context = {}
    return render(request, 'organizeEvent.html', context)

def newEventRequest(request):
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

    return render(request, 'organizeEvent.html')

def register(request):
    events = list()

    for event in Event.objects.all():
        if event.registerbyDate > date.today():
            events.append(event)
        elif event.registerbyDate == date.today() and event.registerbyTime > datetime.now().time():
            events.append(event)

    context = { 'Events' : events }
    return render(request, 'registerEvent.html', context)

def newParticipant(request):
    events = list()

    for event in Event.objects.all():
        if event.registerbyDate > date.today():
            events.append(event)
        elif event.registerbyDate == date.today() and event.registerbyTime > datetime.now().time():
            events.append(event)
    

    new_participant = Participant()
    new_participant.name = request.POST['name']
    new_participant.contact = request.POST['contactNum']
    new_participant.email = request.POST['emailID']
    new_participant.event = Event.objects.get(eventName=request.POST['Event'])
    new_participant.registerType = request.POST['registerType']
    if new_participant.registerType == 'Group':
        new_participant.participantCount = request.POST['participantCount']
    
    new_participant.save()

    context = { 'Events' : events }
    return render(request, 'registerEvent.html', context)

def dashboard(request):
    events = list()
    for event in Event.objects.all():
        if event.endDate > date.today():
            events.append(event)
        elif event.endDate == date.today() and event.endTime > datetime.now().time():
            events.append(event)

    context = { 'events' : events }
    return render(request, 'dashboard.html', context)

def getEventInfo(request):
    error_name = 'No Error'
    try: 
        itm = Event.objects.get(id=request.POST['eventID'])
        if itm.hostpwd != request.POST['eventPassword']:
            itm = 'incorrect Password!!'
        
    except Exception as e:
        itm = None
        error_name = e
    context = { 'event' : itm, 'error_name': error_name }
    return render(request, 'eventInfo.html', context)
