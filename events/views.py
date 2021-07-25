from django.shortcuts import render
from .models import Event

# Create your views here.
def home(rq):
	evs=Event.objects
	return render(rq,'events/home.html',{'events':evs})