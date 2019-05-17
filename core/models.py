from django.db import models


# Create your models here.
class Event(models.Model):
    band = models.CharField(max_length=255)
    datetime_of_performance = models.DateTimeField()
