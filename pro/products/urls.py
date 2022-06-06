from django.urls import path ;
from . import views



urlpatterns = [
	path("create",views.product_create_view,name="create"),
	#path("create1",views.product_create_view1,name="create1"),
	path("initial",views.render_initial_data,name="initial"),
	path("initial1",views.render_initial_data1,name="initial1"),
	path("product/<int:my_id>/",views.dynamic_lookup_view,name="detail"),
	path("",views.product_list_view,name="list"),
	path("owner",views.products_list_view,name="ownerlist"),
	path("delete/<my_id>/",views.products_delete_view,name="delete"),
	path("update/<id>/",views.product_update_view,name="update")
]