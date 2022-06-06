from django import forms
from .models import Resume


JOB_CITY_CHOICE = (("KTM","Kathmandu"),
	("PKR","Pokhara"),
	("BDP","Bhadrapur"),
	("BRG","Birjung"),
	("BRT","Biratnagar"))

GENDER_CHOICES = (("MALE","Male"),
	("FEMALE","Female"),
	("OTHERS","Other"))

class ResumeForm(forms.ModelForm):
	job_city = forms.MultipleChoiceField(
		label="Preferred Job Locations",choices=JOB_CITY_CHOICE,widget=forms.CheckboxSelectMultiple)
	gender = forms.ChoiceField(choices=GENDER_CHOICES,widget=forms.RadioSelect)
	class Meta:
		model = Resume
		fields = ['name','dob','gender','locality','city','state','mobile','email','job_city','profile_image','my_file']
		labels = {"name" : "Full Name","dob":"Date Of Birth","locality":"Address","profile_image":"Profile Picture","my_file":"Document"}
		widgets = {
		"name":forms.TextInput(attrs={'class':'form_control'}),
		"dob" :forms.DateInput(attrs={'class':'form_control'}),
		"locality":forms.TextInput(attrs={'class':'form_control'}),
		"city" : forms.TextInput(attrs={'class':'form_control'}),
		"state" : forms.Select(attrs={'class':'form_control'}),
		"mobile" : forms.NumberInput(attrs={'class':'form_control'}),
		"email" : forms.EmailInput(attrs={'class':'form_control'})
		}