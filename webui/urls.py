from django.urls import path

from webui.views import index

app_name = 'webui'

urlpatterns = [
    path('', index)
]
