from pyexpat import model
from rest_framework import serializers
from stocks.models import Company,Stock

class StockSerializer(serializers.ModelSerializer):
    stock_name = serializers.SlugRelatedField(queryset=Company.objects.all(),slug_field='name')
    class Meta:
        model = Stock
        fields = [
            "id",
            "stock_name",
            "transaction_type",
            "no_of_stocks",
            "price_of_stock",
            "transaction_date"
         ]