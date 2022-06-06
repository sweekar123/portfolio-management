from django.urls import path
from products.api.views import ProductApiView,ProductDetailApiView

urlpatterns = [
    path("",ProductApiView.as_view(),name="papi"),
    path("<pk>",ProductDetailApiView.as_view(),name="papi-detail")
]