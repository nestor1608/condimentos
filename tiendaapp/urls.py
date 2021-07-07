from django.urls import path
from inicioapp import views
from . import views
from django.conf.urls.static import static

urlpatterns = [
    path('tienda',views.tienda,name='tienda'),
]

