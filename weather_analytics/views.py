from django.shortcuts import render

def weather_index(request):

    return render(request, 'weather_analytics/weather_index.html', {})
