from django import forms
from .models import Product
from django.contrib.auth.models import User
from django.conf import settings


class ProductForm(forms.ModelForm):
	title = forms.CharField(label="",widget=forms.TextInput(attrs={"placeholder":"Your title"}))
	description = forms.CharField(required=True,widget=forms.Textarea(attrs={"placeholder":"Your description","class":"new-class-name two","id":"my-id-for-textarea","rows":5,"cols":30}))
	price = forms.DecimalField()
	class Meta:
		model = Product
		fields = ['user','title','image','description','price']

	
	def clean_title(self,*args,**kwargs):
		title = self.cleaned_data.get("title")
		if len(title) > 50:
			raise forms.ValidationError("Title limited")
		else:
			return title

"""	
	def clean_title(self,*args,**kwargs):
		titles = ["shirt","pants","tshirt","vest","shorts","undergarments","tie","coats","suits","halfpants","shocks","shoes"]
		title = self.cleaned_data.get("title")
		for item in range(len(titles)-1):
			if title != titles[item]:
				raise forms.ValidationError("only cloth items in details")
		return title



	def clean_description(self,*args,**kwargs):
		description = self.cleaned_data.get("description")
		if len(description) > 20 :
			raise forms.ValidationError("Description limit exceeded")
		else:
			return description
	"""



"""
class ProductForm1(forms.Form):
	user = forms.ModelChoiceField(queryset=User.objects.all(),empty_label=None)
	title = forms.CharField(max_length=100)
	image = forms.ImageField(required=False)
	description = forms.CharField(max_length=1000)
	price = forms.DecimalField(decimal_places=2,max_digits=10000)
	summary = forms.CharField(max_length=1000)
	featured = forms.BooleanField(required=True)

"""