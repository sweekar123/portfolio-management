from dataclasses import fields
from django import forms
from stocks.models import Stock
from stocks.models import Company

class StockForm(forms.ModelForm):
    class Meta:
        model = Stock
        fields = "__all__"
        labels = {"stock_name":"Name Of Stock","transaction_type":"Action","no_of_stocks":"No of Stocks","price_of_stock":"Price per stock","transaction_date":"Date"}
        
