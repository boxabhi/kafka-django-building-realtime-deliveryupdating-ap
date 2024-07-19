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


from .kafka_producer import send_like_event
from .models import Post

def like_post(request, post_id):
    send_like_event(post_id)
    # post = Post.objects.get(id = post_id)
    # post.likes += 1
    # post.save()
    return JsonResponse({'status': 'like event sent'})
