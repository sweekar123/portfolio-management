from rest_framework import serializers
from products.models import Product
from django.conf import settings
from django.contrib.auth.models import User
class ProductSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(queryset=User.objects.all(),slug_field="username")
    class Meta:
        model = Product
        fields = ["id",
                    'user',
                    'title',
                    'image',
                    'description',
                    'price',
                    'summary',
                    'featured',
                    'updated',
                    'timestamp']