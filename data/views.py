from fileinput import filename
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

import gspread
gc=gspread.service_account(filename='credentials.json')
sh=gc.open_by_key('1GeqprOdvt7H7nFVxM25fEb7t7crRm6TbuD3KSX3Z0c8')
worksheet=sh.sheet1
res=worksheet.get_all_records()
flame_sheet=worksheet.col_values(2)[1:]
smoke_sheet=worksheet.col_values(3)[1:]

print(flame_sheet)
print(smoke_sheet)
print(res[0]['flame sensor'])

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

db=firebase.database()
data=db.child("15-itebVVyWrgPlr5qjMDYk3LNG55fhygj66YDEG9pdw/Sheet1").get().val()
#print(data)

# flame_val=[]
# smoke_val=[]
# for val in data:
# 		print(data[val]['flame_sensor'])
# 		flame_val.append(data[val]['flame_sensor'])
# 		smoke_val.append(data[val]['gas'])

# print(flame_val)

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
    return render(request,'dashboard.html',{'email':request.user.email,'flame_sheet':flame_sheet,'smoke_sheet':smoke_sheet})

def history(request):
	db=firebase.database()
	data=db.child("15-itebVVyWrgPlr5qjMDYk3LNG55fhygj66YDEG9pdw/Sheet1").get().val()
	# flame_val=[]
	# smoke_val=[]
	# time=[]
	# for val in data:
	# 		#print(data[val]['flame_sensor'])
	# 		flame_val.append(data[val]['Flame'])
	# 		smoke_val.append(data[val]['Smoke'])
	# 		time.append(data[val]['Time'])
	# 		# #print(type(data[val]['curr_time']),type(data[val]['flame_sensor']))
	# 		# size=len(data[val]['Time'])
	# 		# list_val=data[val]['Time'][0:size-3].split(":")
	# 		# #tym=""
	# 		# tym = ''.join(list_val)
	# 		# # #print("tym: ",tym," actual: ",data[val]['curr_time'])
	# 		# time.append(int(tym))
	# print(flame_val)
	# print(smoke_val)
	# #print(time)
	# print(time)
	# flame_val.reverse()
	# smoke_val.reverse()
	# time.reverse()
	return render(request,'history.html',{'sensors_data':data})
	#return render(request,'history.html',{'flame_val': flame_val,'smoke_val':smoke_val})



def graph(request):
	db=firebase.database()
	data=db.child("15-itebVVyWrgPlr5qjMDYk3LNG55fhygj66YDEG9pdw/Sheet1").get().val()
	flame_val=[]
	smoke_val=[]
	time=[]
	for key,val in data.items():
			#print(data[val]['flame_sensor'])
			print("key: ",key)
			print("val: ",val)
			flame_val.append(val['Flame'])
			smoke_val.append(val['Smoke'])
			#print(type(data[val]['Date']))
			date_split=key.split(" ")
			date_part=date_split[4]
			time_split=date_part.split(":")
			tym=''.join(time_split)
			print("modified_time: ",time)
			#time.append(key)
			#print(type(data[val]['curr_time']),type(data[val]['flame_sensor']))
			# print("time: ",data[val]['Time']," date: ",data[val]['Date'])
			# size=len(data[val]['Date'])
			# list_val=data[val]['Date'][0:size-3].split(":")
			# # #tym=""
			# tym = ''.join(list_val)
			# #print("tym: ",tym," actual: ",data[val]['curr_time'])
			time.append(int(tym))
	print(flame_val)
	print(smoke_val)
	#print(time)
	# print(time)
	# flame_val.reverse()
	# smoke_val.reverse()
	# time.reverse()
	return render(request,'graph.html',{'flame_val': flame_val,'smoke_val':smoke_val,'time':time})
	#return render(request,'graph.html',{'flame_val': flame_val,'smoke_val':smoke_val})





