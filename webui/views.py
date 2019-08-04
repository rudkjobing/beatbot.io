import json
from typing import List

from django.http import HttpRequest
from django.shortcuts import render

from core.genres import Genre
from core.models import Event
from core.public import get_upcomming_events


def index(request: HttpRequest):
    events: List[Event] = get_upcomming_events()

    serialized_events = [{
        'venue': event.venue,
        'artist': event.artist,
        'datetime_of_performance': event.datetime_of_performance.isoformat(),
        'ticket_price': float(event.ticket_price.amount),
        'genres': [Genre[genre].name for genre in event.genres],
        'source': event.source_url,
        'description': event.description
    } for event in events]

    return render(request, "index.html", {
        "title": "BeatBot.io",
        "props": json.dumps({"upcomming_events": serialized_events})
    })
