from django.utils import timezone

from core.models import Event


def get_upcomming_events():
    return Event.objects.filter(datetime_of_performance__gt=timezone.now())