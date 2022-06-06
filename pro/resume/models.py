from django.db import models

# Create your models here.
STATE_CHOICE = (
	("Provience 1","Provience 1"),("Madesh","Madesh"),("Bagmati","Bagmati"),("Gandaki","Gandaki"),("Karnali","Karnali"),("Provience 7","Provience 7")
	)
GENDER_CHOICES = (("MALE","Male"),
	("FEMALE","Female"),
	("OTHERS","Other"))
def upload_image_to(instance,filename):
	return "resumes/{user}/{filename}".format(user=instance.user,filename=filename)

def upload_file_to(instance,filename):
	return "resumes/{user}/{filename}".format(user=instance.user,filename=filename)

class Resume(models.Model):
	name = models.CharField(max_length=200)
	dob = models.DateField(auto_now=False, auto_now_add = False)
	gender = models.CharField(choices=GENDER_CHOICES,max_length=100)
	locality = models.CharField(max_length=100)
	city = models.CharField(max_length=100)
	state = models.CharField(choices=STATE_CHOICE,max_length=50)
	mobile = models.PositiveBigIntegerField()
	email = models.EmailField()
	job_city = models.CharField(max_length=100)
	profile_image = models.ImageField(upload_to=upload_image_to,blank=True)
	my_file = models.FileField(upload_to=upload_file_to)
	updated = models.DateTimeField(auto_now=True)
	timestamp = models.DateTimeField(auto_now_add=True)


	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return f"resume/{self.id}"


