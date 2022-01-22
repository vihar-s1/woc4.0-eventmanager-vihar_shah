"""event_manager URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls.conf import path
from event_manager_app import views

urlpatterns = [
    path('', views.index, name='index'),

    path('index/organize-event', views.organize, name='organize'),
    path('index/register-event', views.register, name='register'),

    path('index/dashboard', views.dashboard, name='dashboard'),
    path('index/organize-event/form-submission', views.newEventRequest, name='newEvent'),
    
    path('index/register-event/form-submission', views.newParticipant, name='newParticipant'),
    path('index/dashboard/get-event-info', views.getEventInfo, name='getEventInfo')
]
