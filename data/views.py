from django.shortcuts import render
from django.http import HttpResponse
from .models import *
import random
import pyrebase
import datetime;

config = {
    'apiKey': "AIzaSyBV3jP5cl1AVP3HgO6_1J_wrjyffqQUfko",
    'authDomain': "iotproject-2800f.firebaseapp.com",
    'databaseURL': "https://iotproject-2800f-default-rtdb.firebaseio.com",
    'projectId': "iotproject-2800f",
    'storageBucket': "iotproject-2800f.appspot.com",
    'messagingSenderId': "863247827424",
    'appId': "1:863247827424:web:ba640e5eabf0b412062b85",
    'measurementId': "G-727CF3R175"
  }
firebase=pyrebase.initialize_app(config)
# Create your views here.





def home(request):
    return render(request,'data/dashboard.html')

def history(request):
    #sensors_data = sensor_info.objects.all()
    #print("sensors_data: ")
    #print(sensors_data.values())
    #<QuerySet [{'id': 4, 'flame_val': 12.0, 'smoke_val': 23.0, 'temp_val': 34.0, 'date_created': datetime.time(10, 45, 41, 14967)}]>

    #for data in sensors_data.values():
    #  print(data['flame_val'],data['smoke_val'])
    db=firebase.database()
    data=db.child("sensor_data").get().val()
    #print(data)
    return render(request,'data/history.html',{'sensors_data': data})

