from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User,auth
from django.contrib import messages

# Create your views here.

def home(request):
	result = request.user.is_authenticated
	if result is True:
		return render(request,"new1/home.html")
	else:
		return render(request,"new1/login.html")

def about(request):
	return render(request,'new1/about.html')

def contact(request):
	return render(request,'new1/contact.html')

def portfolio(request):
	return render(request,'new1/portfolio.html')

def login(request):
	if request.method == "POST":
		username = request.POST["username"]
		password = request.POST["password"]
		user = auth.authenticate(username=username,password=password)
		if user is not None:
			auth.login(request,user)
			return redirect("home")
		else:
			messages.info(request,"Invalid Credentials")
			return redirect("login")
	return render(request,'new1/login.html')

def register(request):
  	if request.method == "POST":
  		first_name = request.POST["first_name"]
  		last_name = request.POST["last_name"]
  		username = request.POST["username"]
  		email = request.POST["email"]
  		password1 = request.POST["password1"]
  		password2 = request.POST["password2"]
  		if password1 == password2:
  			if User.objects.filter(username=username).exists():
  				messages.info(request,"Username already exists")
  				return redirect("register")
  			elif User.objects.filter(email=email).exists():
  				messages.info(request,"Email already exists")
  				return redirect("register")
  			else:
  				user = User.objects.create_user(username=username,email=email,password=password1,first_name=first_name,last_name=last_name)
  				user.save();
  				print("User Created")
  				messages.info(request,"User Created. Try to login")
  				return redirect("login")
  		else:
  			messages.info(request,"Password isn't matching")
  			return redirect("register")
  	else:
  		return render(request,"new1/register.html")

  	return render(request,"new1/register.html")


def logout(request):
	auth.logout(request)
	return redirect("home")
