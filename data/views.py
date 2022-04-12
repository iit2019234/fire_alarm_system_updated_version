from django.shortcuts import render
from django.http import HttpResponse
from .models import *
import random
import pyrebase
from django.shortcuts import get_object_or_404, render
import datetime;
from django.utils.html import strip_tags
from django.urls import reverse, reverse_lazy
from django.shortcuts import render,HttpResponse
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.template.loader import render_to_string, get_template
from django.core.mail import send_mail
from .forms import *
from templates import *
from django.core.mail import EmailMessage
from django.core.mail import EmailMultiAlternatives


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

def index(request):
    return render(request,'index.html')

def registerPage(request):
	if request.user.is_authenticated:
		return HttpResponseRedirect('/')
	else:
		form = CreateUserForm()
		if request.method == 'POST':
			form = CreateUserForm(request.POST)
			if form.is_valid():
				form.save()
				user = form.cleaned_data.get('username')
				return HttpResponseRedirect('/loginpage')
		context = {'form':form}
		return render(request, 'signup.html', context)

def loginpage(request):
	if request.user.is_authenticated:
		return render(request, 'dashboard.html',{'email':request.user.email})
	else:
		if request.method == 'POST':
			username = request.POST.get('username')
			password =request.POST.get('password')

			user = authenticate(request, username=username, password=password)

			if user is not None:
				login(request, user)
				return render(request, 'dashboard.html',{'email':request.user.email})
			else:
				messages.info(request, 'invalid credentials')
		return render(request, 'login.html')

def logoutuser(request):
    logout(request)
    return render(request,'index.html')

def dashboard(request):
    return render(request,'dashboard.html',{'email':request.user.email})

def history(request):
    db=firebase.database()
    data=db.child("sensor_data").get().val()
    #print(data)
    return render(request,'history.html',{'sensors_data': data})

