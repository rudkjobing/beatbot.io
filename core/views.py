from django.http import HttpRequest, JsonResponse

# Create your views here.
from django.utils import timezone

from core.models import Event


def upcomming_events(request: HttpRequest):
    events = Event.objects.filter(datetime_of_performance__gt=timezone.now())

    serialized_events = [{
        'venue': event.venue,
        'artist': event.artist
    } for event in events]

    return JsonResponse(data=serialized_events, safe=False)
