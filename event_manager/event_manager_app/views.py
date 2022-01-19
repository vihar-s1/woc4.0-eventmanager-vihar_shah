from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.
def index(request):
    template = loader.get_template('index.html')
    context = {
        'message' : 'site under construction!'
    }
    return HttpResponse(template.render(context, request))
    #or comment line 7 and 9 and uncomment just below one
    #return render(request, 'index.html',context)

def organize(request):
    context = {}
    return render(request, 'organizeEvent.html', context)

def register(request):
    context = {}
    return render(request, 'registerEvent.html', context)

def dashboard(request):
    context = {}
    return render(request, 'dashboard.html', context)
