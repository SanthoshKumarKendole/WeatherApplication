from django.shortcuts import render

# Create your views here.
import urllib.request
import json
def sample(request):
    if request.method=='POST':
        city=request.POST['city']
        source=urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q=' + city + '&units=metric&appid=51bc024c81faeb5f294ac61e0846792a').read()
        weather=json.loads(source)
        data={
            "countrycode":str(weather['sys']['country']),
            "coordinate" :str(weather['coord']['lon'])+', ' +str(weather['coord']['lat']),
            "temp":str(weather['main']['temp']),
            "pressure":str(weather['main']['pressure']),
            "humidity":str(weather['main']['humidity']),
            "main":str(weather['weather'][0]['main']),
            "description":str(weather['weather'][0]['description']),
            "icon":weather['weather'][0]['icon'],
        }
        print(data)
    else:
        data={}
    return render(request,'weather.html',data)