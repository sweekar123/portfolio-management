from urllib import request, response
from django.shortcuts import get_object_or_404, render,redirect
from stocks.models import Stock,Company
from rest_framework import generics
from rest_framework.response import Response
from stocks.api.serializers import StockSerializer
from rest_framework.views import APIView

class StockListSearchAPIView(APIView):
    permission_classes = []
    authentication_classes = []

    def get(self,request,format=None):
        qs = Stock.objects.all()
        serializer = StockSerializer(qs,many=True)
        return Response(serializer.data)

    def post(self,request,format=True):
        qs = Stock.objects.all()
        serializer = StockSerializer(qs,many=True)
        return Response(serializer.data)

