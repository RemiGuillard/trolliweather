import requests

from .models import City

def poll_weather(request):

    r = requests.get()
