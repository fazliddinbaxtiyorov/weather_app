from django.shortcuts import render

from django.http import HttpResponse

from requests import get
from datetime import datetime


# Create your views here.
def home(request):
    return HttpResponse('<h2>Weather App</h2>')


def weather_info(request, city):
    cities = city
    url = get(f"https://goweather.herokuapp.com/weather/{cities}").json()
    res = url
    temp = res['temperature']
    wind = res['wind']
    desc = res['description']
    date = datetime.now().date()

    return render(request, 'weather/index.html',
                  context={'temp': temp, 'wind': wind, 'desc': desc, 'date': date, 'city': city})
