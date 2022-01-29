from django.shortcuts import render
from event_manager_app.models import *
from datetime import date, datetime
from django.contrib import messages
from django.conf import settings
from django.core.mail import send_mail
from twilio.rest import Client

# Create your views here.
def index(request):
    for events in Event.objects.all():
        if events.endDate < date.today():
            events.delete()
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

    events = Event.objects.all()

    isNewEvent = True

    for event in events:
        if event.eventName == new_event.eventName and event.hostEmail == new_event.hostEmail:
            isNewEvent = False
            break
    
    if isNewEvent:
        new_event.save()
        messages.success(request, "New Event Registered!!")

        # uncomment below code to activate mail
        '''subject = "New Event Registered"
        message = "Thank For Organizing Event Through our Site!!\n\n"
        message = message + f"Event Name: {new_event.eventName}\nStarts From: {new_event.startDate}, {new_event.startTime}\n"
        message = message + f"\nEnds On: {new_event.endDate}, {new_event.endTime}"
        message = message + f"\nLocation: {new_event.location}"
        message = message + f"\nRegister By: {new_event.registerbyDate}, {new_event.registerbyTime}"
        message = message + "\n\nRegards,\nEvent Management Website"
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [new_event.hostEmail, ]
        send_mail( subject, message, email_from, recipient_list )'''

    else:
        messages.error(request, "Event already registered for the given Email!!")

    return render(request, 'organizeEvent.html')


def register(request):
    events = list()

    for event in Event.objects.all():
        if event.registerbyDate > date.today():
            events.append(event)
        elif event.registerbyDate == date.today() and event.registerbyTime > datetime.now().time():
            events.append(event)

    if len(events) == 0: events = None

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
    new_participant.event = Event.objects.get(id=request.POST['Event'])
    new_participant.registerType = request.POST['registerType']
    if new_participant.registerType == 'Group':
        new_participant.participantCount = request.POST['participantCount']
    
    newRegister = True
    event = Event.objects.get(id=request.POST['Event'])

    for participant in event.participant_set.all():
        if participant.email == new_participant.email:
            newRegister = False
            break

    if newRegister:
        new_participant.save()
        messages.success(request, "Participant Registration Successful!!")
        
        # Uncomment below code to activate mail and sms
        '''subject = 'Registered For the Event.'
        message = f"You have registered for {new_participant.event.eventName},\n"
        message = message + f"Held from {new_participant.event.startDate} to {new_participant.event.endDate} at {new_participant.event.location}.\n"
        message = message + f"\nYour participant ID is {new_participant.id}."
        message = message + "\n\nRegards,\nEvent Management Website"
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [new_participant.email, ]
        send_mail( subject, message, email_from, recipient_list )

        try:
            client = Client( settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN )
            client.messages.create( from_=settings.TWILIO_NUMBER, to=new_participant.contact, body=message )
        except:
            pass #unwanted error due to free account

        subject = 'new Participant Registered.'
        message = f"New participant has registered for the event \'{new_participant.event}\'.\n\n"
        message = message + f"Name: {new_participant.name}\nContact: {new_participant.contact}\nEmail: {new_participant.email}\n"
        message = message + f"Registration Type: {new_participant.registerType}\nParticipant Count: {new_participant.participantCount}"
        message = message + "\n\nRegards,\nEvent Management Website"
        recipient_list = [new_participant.event.hostEmail, ]
        send_mail( subject, message, email_from, recipient_list )'''

    else:
        messages.error(request, "Email already registered under this Event!!")


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
