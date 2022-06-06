from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path("",include("new1.urls")),
    path("products/",include("products.urls")),
    path("resume/",include("resume.urls")),
    path("stocks/",include("stocks.urls")),
    path("stocks/api/",include("stocks.api.urls")),
    path("products/api/",include("products.api.urls"))
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)