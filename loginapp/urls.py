from django.urls import path
from django.contrib.auth.views import LoginView,LogoutView,logout_then_login,
from django.views.generic.base import View
from inicioapp import views


urlpatterns = [
    path('login/', name='login'),
    path('logout',name='logout'),
    
    
]
