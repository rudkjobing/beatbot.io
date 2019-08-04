from django.urls import path

from core.views import upcomming_events
from webui.views import index

app_name = 'webui'

urlpatterns = [
    path('', index)
]
