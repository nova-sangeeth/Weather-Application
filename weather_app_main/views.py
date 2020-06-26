from django.shortcuts import render, redirect
import requests
from .models import City
from .forms import CityForm

# Create your views here.
def index(request):
    # cities can be called because the verbose plural name is used  as a meta in models.py
    cities = City.objects.all()
    # the url and the api key
    url = "http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=271d1234d3f497eed5b1d80a07b3fcd1"
    city = City.objects.all()

    if request.method == "POST":
        form = CityForm(request.POST)
        form.save()
    form = CityForm()
    weather_data = []
    for city in cities:
        city_weather = requests.get(url.format(city)).json()

        weather = {
            "city": city,
            "temperature": city_weather["main"]["temp"],
            "humidity": city_weather["main"]["humidity"],
            "wind_speed": city_weather["wind"]["speed"],
            "description": city_weather["weather"][0]["description"],
            "icon": city_weather["weather"][0]["icon"],
        }
        weather_data.append(weather)  # the typo line " used a . instead of _"

    context = {"weather_data": weather_data, "form": form}

    return render(request, "weather/index.html", context)


# code to render the delete functionality to remove the cities which are not wanted in the list rendered on the main page.


def delete(request, pk):
    City.objects.filter(id=pk).delete()
    city_items = City.objects.all()
    return render(request, "/", {"city_items": city_items})
