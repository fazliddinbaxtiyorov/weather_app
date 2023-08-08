from django.urls import path

from weather import views

urlpatterns = [
    path('', views.home, name='weather-home'),
    path('weather/<str:city>', views.weather_info),
]
