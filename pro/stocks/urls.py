from django.urls import  path
from stocks.views import stock_add_view,stock_list_view,overall_stock_dashboard,individual_stock_dashboard,stock_update_view,stock_delete_view
urlpatterns = [
    path("add",stock_add_view,name="stock-add"),
    path("",stock_list_view,name="stock-list"),
    path("overallstock",overall_stock_dashboard,name="overall"),
    path("individual",individual_stock_dashboard,name="individual"),
    path("update/<id>",stock_update_view,name="stock-update"),
    path("delete/<id>",stock_delete_view,name="stock-delete")
]