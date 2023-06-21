from django.shortcuts import render
import json
import urllib.request

# Create your views here.


appid = 'ba011cfa6f5a1ba0d8ec1c3a2868f257'

def index(request):
    if request.method == "POST":
        city = request.POST ['city']
        res = urllib.request.urlopen("https://api.openweathermap.org/data/2.5/weather?q=" + city + "&appid=" + appid).read()
        json_data = json.loads(res)
        data = {
            "country_code":str(json_data['sys']['country']),
            "coordinate": str(json_data['coord']['lon'])+' '+str(json_data['coord']['lat']),
            "temp": str(json_data['main']['temp'])+'k',
            "pressure": str(json_data['main']['pressure']),
            "humidity": str(json_data['main']['humidity']),
        }
    else:
        city = ' '
        data= {}
    return render(request, 'index.html',{'city':city, 'data' :data})