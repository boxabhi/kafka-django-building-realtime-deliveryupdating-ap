# tracker/views.py
from django.http import JsonResponse
from .models import LocationUpdate
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')

def latest_location(request):
    latest_update = LocationUpdate.objects.latest('timestamp')
    return JsonResponse({
        'latitude': latest_update.latitude,
        'longitude': latest_update.longitude,
        'timestamp': latest_update.timestamp
    })

