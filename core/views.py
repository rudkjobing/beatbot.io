from django.http import HttpRequest, JsonResponse

# Create your views here.
from django.utils import timezone

from core.models import Event
from core.public import get_upcomming_events


def upcomming_events(request: HttpRequest):
    events = get_upcomming_events()

    serialized_events = [{
        'venue': event.venue,
        'artist': event.artist
    } for event in events]

    return JsonResponse(data=serialized_events, safe=False)
