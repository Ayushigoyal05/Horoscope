import requests
from django.shortcuts import render
from .models import Horoscope
import base64
import json

apiKey='d99bcbe843e2f607e58ec5ff0c2b8f5e'
url='https://json.astrologyapi.com/v1/daily_nakshatra_prediction'
userId='612924'

def home(request):
    if request.method == "POST":
        name=request.POST.get('name','')
        date=request.POST.get('date','')
        
        [year, month, day] = date.split('-')

        print(date, 'date')
        
        data = {
            'year': year,
            'day': day,
            'month':month,
		  	'hour':2,
			'min':23,
			'lat':19.132,
			'lon':72.342,
			'tzone':5.5
	    }

        authKey = userId+":"+apiKey
        
        headers = {
            "Content-Type":"application/json",
            "authorization": 'Basic NjEyOTI2OmY1MTFiNjJkNDIwZTA2YWMzYjY4NzFlZGE2MjVmYTA5'
        }
        
        resp = requests.post(url, headers=headers, data=json.dumps(data))

        print(resp.status_code)
        print(resp.text)
        resp_data = resp.json()

        # print(resp_data['birth_moon_sign'])
        contact=Horoscope(name=name,date=date)
        contact.save()
        return render(request, "index.html", {'horoscope':resp_data})
    return render(request, "base.html")

def index(request):
	return render(request,'index.html')
# Create your views here.
