from django.shortcuts import render
from django.conf import settings
import requests
from django.contrib import messages
# Create your views here.

def index(request):
    context = {}        
    API_KEY = settings.API_KEY
    if request.method == 'POST':
        city = request.POST.get('city')
        api_url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric'
        response = requests.get(api_url)
        
        if response.status_code == 200:
            data = response.json()
            temperature = data['main']['temp']
            humidity = data['main']['humidity']
            wind_speed = data['wind']['speed']
            icon = data['weather'][0]['icon']
            main = data['weather'][0]['main']
            
            context = {
                'city': city,
                'temperature': temperature,
                'humidity': humidity,
                'wind_speed': wind_speed,
                'icon': icon,
                'main': main
            }
            return render(request, 'index.html', context)
        
        else:
            messages.error(request,'invalid city name')
        
    return render(request, 'index.html')

def test_404(request):
    return render(request, '404.html', status=404)