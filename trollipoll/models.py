from django.db import models

class City(models.Model):
    city_name = models.CharField(max_length=64)
    country_name = models.CharField(max_length=64)
    time_interval = models.IntegerField(default=24) # in hour
    api_location = models.CharField(max_length=200)

