from django.urls import path

from core.views import upcomming_events

app_name = 'core'

urlpatterns = [
    path('upcomming-events', upcomming_events)
]
