from django.shortcuts import render,redirect,get_object_or_404
from .forms import ProductForm
#from .forms import ProductForm1
from .models import Product


# Create your views here.

#this is a view for form.Modelform
def product_create_view(request,*args,**kwargs):
	if request.user.is_authenticated:
		if request.method == "POST":
			form = ProductForm(request.POST,request.FILES)
			if form.is_valid():
				form.save()
				return redirect("list")
			else:
				form = ProductForm(request.POST,request.FILES)
				context = {
					"form" : form
				} 
				return render(request,"products/product_create_view.html",context)
		else:
			form = ProductForm()
			context = {
				"form" : form
			}
			return render(request,"products/product_create_view.html",context)
	else:
		return redirect("login")



"""
##this is a view for form.Forms 
def product_create_view1(request):
	form = ProductForm1()
	if request.method == "POST" :
		form = ProductForm1(request.POST)
		if form.is_valid():
			#print(form.cleaned_data)
			Product.objects.create(**form.cleaned_data)
			return redirect("create1")
		else:
			print(form.errors)
			context = {
				"form" : form
			}

			return render(request,"products/product_create_view.html",context)
	else:
		context = {
			"form" : form
		}
		return render(request,"products/product_create_view.html",context)

"""

#views for initial_custom checking data
def render_initial_data(request):
	initial_data = {
		"title" : "This is good",
		"description" : "Nice shit",
		"image" : "new1/images/sweekar.jpg",
		"price" : 122.12
		}
	form = ProductForm(request.POST or None,initial = initial_data)
	context = {
	'form' : form
	}
	return render(request,"products/product_create_view.html",context)


#views for obj as initial data 
def render_initial_data1(request):
	obj = Product.objects.get(id=2)
	form = ProductForm(request.POST or None,instance=obj)
	if form.is_valid():
		form.save()
		return redirect("create")
	context = {
		"form" : form
	}
	return render(request,"products/product_create_view.html",context)


#views for dynamic lookup 
def dynamic_lookup_view(request,my_id):
	obj = get_object_or_404(Product,id=my_id)
	context = {
		"obj" : obj
	}
	return render(request,"products/product_detail.html",context)


def product_list_view(request,*args,**kwargs):
	queryset = Product.objects.all()
	print(request.user)
	context = {
		"objects" : queryset
	}
	return render(request,"products/productsgeneral.html",context)

"""
def products_list_view(request):
	queryset = Product.objects.filter(user = request.user)
	print(queryset)
	context = {
		"objects" : queryset
	}
	return render(request,"products/product_list.html",context)
"""


def products_list_view(request):
	if request.user.is_authenticated:
		queryset = Product.objects.filter(user = request.user)
		context = {
			"objects" : queryset
		}
		return render(request,"products/product_list.html",context)
	else:
		return redirect("login")


def products_delete_view(request,my_id):
	if request.user.is_authenticated:
		obj = get_object_or_404(Product,id=my_id)
		if request.user == obj.user:
			if request.method == "POST":
				obj.delete()
				return redirect("ownerlist")
			else:
				context = {
					"object" : obj
				}
				return render(request,"products/product_delete.html",context)
		else:
			return redirect("list")
	return redirect("login")


def product_update_view(request,id):
	if request.user.is_authenticated:
		obj = get_object_or_404(Product,id=id)
		if request.user == obj.user:
			if request.method == "POST":
				form = ProductForm(request.POST,request.FILES,instance=obj)
				if form.is_valid():
					form.save()
					return redirect("ownerlist")
				else:
					form = ProductForm(instance=obj)
					context = {
						"form" : form
					}
					return render(request,"products/product_create_view.html",context)
			else:
				form = ProductForm(instance=obj)
				context = {
					"form" : form
				}
				return render(request,"products/product_create_view.html",context)
		else:
			return redirect("ownerlist")
	else:
		return redirect("login")



"""

def product_update_view(request,id):
	obj = Product.objects.get(id=id)
	print(obj.image)
	form = ProductForm(request.POST or None,instance=obj)
	if form.is_valid():
		form.save()
	context = { 
		"form" : form
	}
	return render(request,"products/product_create_view.html",context)
"""




