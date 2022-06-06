from django.contrib import admin
from stocks.models import Stock
from stocks.models import Company
# Register your models here.
admin.site.register(Company)

@admin.register(Stock)
class StockAdmin(admin.ModelAdmin):
    list_display = ["id",'stock_name','transaction_type',"no_of_stocks","price_of_stock","transaction_date"]


