
from django.urls import path
from inicioapp import views
from django.conf.urls.static import static



urlpatterns = [
    
    path('',views.inicio, name= 'index'),
]