from django.urls import path,include
from . import views

urlpatterns = [
	path("",views.home,name="home"),
	path("portfolio",views.portfolio,name="portfolio"),
	path("contact",views.contact,name="contact"),
	path("about",views.about,name="about"),
	path("register",views.register,name="register"),
	path("login",views.login,name="login"),
	path("logout",views.logout,name="logout")
]
