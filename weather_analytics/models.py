from django.db import models
from django.utils import timezone


class WeatherSource(models.Model):

    name = models.TextField()
    source_uri = models.URLField()
    poll_frequency = models.TimeField()

    def __str__(self):
        return self.name

class WeatherPrediction(models.Model):

    temperature = models.IntegerField
    published_date = models.DateTimeField()
    source = models.ForeignKey('WeatherSource')

    def __str__(self):
        return "(): ()".format(self.published_date, self.temperature)
