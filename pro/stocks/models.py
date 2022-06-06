from pyexpat import model
from django.db import models

class Company(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


# Create your models here.
TYPE_CHOICES = ( ("BUY","BUY"),("SELL","SELL") )
#STOCK_CHOICES = ( ("HIDCL","HIDCL"),("KSBBL","KSBBL"),("MLBL","MLBL"),("API","API"),("FMDBL","FMDBL"),("JBBL","JBBL"),("MLBSL","MLBSL"),("SHEL","SHEL"),("MEN","MEN"),("LIC","LIC"),("NRIC","NRIC"))

class Stock(models.Model):
    stock_name = models.ForeignKey(Company,on_delete=models.CASCADE)
    transaction_type = models.CharField(choices=TYPE_CHOICES,max_length=10)
    no_of_stocks = models.IntegerField()
    price_of_stock = models.DecimalField(decimal_places=2,max_digits=7)
    transaction_date = models.DateField()

    def __instance__(self):
        return self.stock_name
    
    def get_absolute_url(self):
        return f"/stocks/update/{self.id}"

    @property
    def investment(self):
        return self.no_of_stocks * 100 
    
    @property
    def current_amount(self):
        return self.no_of_stocks * self.price_of_stock
    
    @property
    def profit(self):
        return self.no_of_stocks * self.price_of_stock - self.no_of_stocks * 100
    


    







