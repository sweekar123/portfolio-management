from django.urls import path
from stocks.api.views import StockListSearchAPIView

urlpatterns = [
    path("",StockListSearchAPIView.as_view(),name="sapi")
]