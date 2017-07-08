from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from .forms import *
from .models import *
from .HEOM import *

# Create your views here.
def index(request):
	return render(request, "sarpenstein/index.html", {})

def laptops(request):
	devices = Device.objects.filter(Device_type='Laptop')
	return render(request, 'sarpenstein/laptops.html', {'devices':devices})

def home(request):
	return render(request, 'sarpenstein/home.html', {})

def hp(request):
	return render(request, 'sarpenstein/hp.html', {})

def list_products(request):
	devices  = Device.objects.all()
	return render(request, 'sarpenstein/list_products.html', {"devices":devices})

def brand_category(request, b):
	
	devices  = Device.objects.filter(Brand_name__exact=b)
	return render(request, 'sarpenstein/tecno.html', {"devices":devices})
def search(request):
	return render(request, 'sarpenstein/search.html', {})

def product(request):
	Brand_names = Device.objects.values('Brand_name').distinct()
	Device_types = Device.objects.values('Device_type').distinct()
	data = ''
	# try:
	if request.GET['device_type'] == '':
		Device_type = None
	else:
		Device_type = request.GET['device_type']
		

	if request.GET['brand_name'] == '':
		Brand_name = None
	else:
		Brand_name = request.GET['brand_name']

	if request.GET['ram'] == '':
		RAM = None
	else:
		RAM = int(request.GET['ram'])

	if request.GET['storage_size'] == '':
		Storage_size = None
	else:
		Storage_size = int(request.GET['storage_size'])

	if request.GET['screen_size'] == '':
		Screen_size = None
	else:
		Screen_size = int(request.GET['screen_size'])

	if request.GET['cost'] == '':
		Cost = None
	else:
		Cost = int(request.GET['cost'])

	search_result=Device.objects.filter(Brand_name = Brand_name)#Device_type=Device_type)
	data = Device.objects.all()
	return render(request, 'sarpenstein/results.html', {'search_result': search_result})
	# heom_obj = HEOMClass(497458, 134)
	# heom_score_list = []
	# for device in data:
	# 	scores_list = []
	# 	scores_list.append(heom_obj.h_i(Device_type, Device.Device_type, "categorical"))
	# 	scores_list.append(heom_obj.h_i(Brand_name, Device.Brand_name, "categorical"))
	# 	scores_list.append(heom_obj.h_i(RAM, Device.RAM, "categorical"))
	# 	scores_list.append(heom_obj.h_i(Storage_size, Device.Storage_size, "categorical"))
	# 	scores_list.append(heom_obj.h_i(Screen_size, Device.Screen_size, "categorical"))
	# 	scores_list.append(heom_obj.h_i(Cost, Device.Cost, "regular"))
	# 	heom_score_list.append([Device.id, heom_obj.heom(scores_list)])

	# sorted_heom_score_list = sorted(heom_score_list, key=lambda x: x[1])[0:10]
	# search_result = []
	# for x in sorted_heom_score_list:
	# 	b = Device.objects.get(pk = int(x[0]))
	# 	search_result.append(b)
	# 	print(x, b)
	# return render(request, 'sarpenstein/results.html', {'search_result': search_result})
	# except TypeError:
	# 	if request.user.is_authenticated:
	# 		return render (request, 'sarpenstein/search.html', {'error': 'Wrong Data Type Entered for an Integer Field', 'Brand_names': Brand_names, 'Device_types' : Device_types})
	# 	return render (request, 'sarpenstein/search.html', {'error': ' Wrong Data Type Entered for an Integer Field', 'Brand_names': Brand_names, 'Device_types' : Device_types})
	# # return render(request, 'sarpenstein/search.html', {'data': data, 'request': request})


def register(request):
	form = RegisterForm(request.POST or None)
	if request.user.is_authenticated:
		return HttpResponseRedirect('/home')
	if request.method == 'POST':
		if form.is_valid():
			user = form.save()
			user.refresh_from_db()  # load the profile instance created by the signal
			user.save()
			raw_password = form.cleaned_data.get('password1')
			user = authenticate(username=user.username, password=raw_password)
			login(request, user)
			return HttpResponseRedirect('/home')
	else:
		form2 = RegisterForm(request.POST or None)
	return render(request, 'sarpenstein/register.html', {'form': form})

def login(request):
	if request.user.is_authenticated:
		return HttpResponseRedirect('/home')
	form = LoginForm(request.POST or None)
	if form.is_valid():
		username = form.cleaned_data.get('username')
		password = form.cleaned_data.get('password')
		user = authenticate(username=username, password=password)
		login(request, user)
		return HttpResponseRedirect('/home')
	return render(request, 'sarpenstein/login.html', {'form': form})

def logout(request):
	logout(request)
	return HttpResponseRedirect('/')

def home2(request):
	return render(request, 'sarpenstein/home2.html', {})