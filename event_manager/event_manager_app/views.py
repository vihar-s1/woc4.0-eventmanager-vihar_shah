from django.shortcuts import render
from event_manager_app.models import Event

# Create your views here.
def index(request):
    context = {
        'message' : 'site under construction!'
    }
    return render(request, 'index.html',context)

def organize(request):
    context = {}
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
