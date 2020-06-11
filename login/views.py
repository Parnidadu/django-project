from django.shortcuts import render
from django.contrib.auth import login,authenticate
from django.contrib.auth.forms import UserCreationForm
from .forms import signUpForm, loginForm, customers
from django.http import HttpResponseRedirect, HttpResponse, request, JsonResponse
from .models import Profile
from django.shortcuts import render, redirect, reverse
# Create your views here.
from django.contrib import messages

def index(request):
	return render(request,'base.html')

def login(request):
	form = signUpForm()
	if request.method=='POST':
		form = signUpForm(request.POST)
		profile_objects = (Profile.objects.all())
		email = str(form['email'].value())
		password = str(form['password'].value())
		if Profile.objects.filter(email=email,password=password):
			objects = Profile.objects.filter(email=email,password=password)
			# return HttpResponse("Welcome {}".format(objects.values()[0]['first_name']))
			context = {
				'first_name': objects.values()[0]['first_name'],
				'last_name' : objects.values()[0]['last_name'],
				'email'     : objects.values()[0]['email'],
				'image' 	: objects.values()[0]['image']
			}
			return render(request,'profile.html',context)
		else:
			print(profile_objects)
			return JsonResponse({'error':"Wrong Id or password"})

	context = {
		'form':form
	}
	return render(request,'login.html',context)

def register(request):
	form = signUpForm()
	if request.method=="POST":
		form = signUpForm()
		if form.is_valid():
			form.save(commit=True)
			return redirect('login:index')
			
	context = {
		"form":form
	}	
	return render(request,'register.html',context)


def about(request):
	return render(request,'about.html')

def logout(request):
	return HttpResponse("You are logged out")



