from django.db import models
from django.conf import settings
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.

def upload_to_product(instance,filename):
	return "product/{user}/{filename}".format(user=instance.user,filename=filename)

class Product(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
	title = models.CharField(max_length=200)
	image = models.ImageField(upload_to = upload_to_product)
	description = models.TextField(blank = True,null = True)
	price = models.DecimalField(decimal_places=2,max_digits=10000)
	summary = models.TextField(blank=False,null=False)
	featured = models.BooleanField(default=False)
	updated = models.DateTimeField(auto_now=True)
	timestamp = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return f"product/{self.id}/"

	#def get_absolute_url(self):
	#	return reverse("products : detail",kwargs={"id":self.id})