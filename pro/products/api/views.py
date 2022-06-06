from importlib.resources import contents
import json
from urllib import request
from django.shortcuts import get_object_or_404, render,redirect
from products.api.serializers import ProductSerializer
from rest_framework import generics,mixins
from products.models import Product

class ProductApiView(generics.ListAPIView):
    permission_classes = []
    authentication_classes = []
    serializer_class = ProductSerializer

    def get_queryset(self):
        qs = Product.objects.all()
        query = self.request.GET.get('q')
        if query is not None:
            qs = qs.filter(content__icontains=query)
        return qs
    
    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)
    
class ProductDetailApiView(mixins.DestroyModelMixin,mixins.UpdateModelMixin,generics.RetrieveAPIView):
    permission_classes = []
    authentication_classes = []
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def put(self,request,*args,**kwargs):
        return self.update(request,*args,**kwargs)

    def delete(self,request,*args,**kwargs):
        return self.destroy(request,*args,**kwargs)
    
    def patch(self,request,*args,**kwargs):
        return self.update(request,*args,**kwargs)
    



