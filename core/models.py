from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField
from django.db import models

from djmoney.models.fields import MoneyField


class Event(models.Model):
    venue = models.CharField(max_length=255)
    source_url = models.URLField(max_length=255)
    artist = models.CharField(max_length=255)
    ticket_price = MoneyField(max_digits=10, decimal_places=2, default_currency='DKK')
    datetime_of_performance = models.DateTimeField()
    raw_genres = ArrayField(models.CharField(max_length=255, blank=True))
    genres = ArrayField(models.CharField(max_length=255, blank=True))
    description = models.TextField(default="")

    class Meta:
        unique_together = ('venue', 'artist', 'datetime_of_performance',)
