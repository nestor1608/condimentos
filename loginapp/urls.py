from django.urls import path
from django.contrib.auth.views import LoginView,LogoutView, logout_then_login
from django.views.generic.base import View
from inicioapp import views


urlpatterns = [
    path('login/',LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/',LogoutView,name='logout'),
    path('password_change/', name ='password_change'),
    path('passwor d_change/done/', name='password_change_done'),
    path('passwor d_reset/', name='password_reset'),
    path('passwor d_reset/done/', name='password_reset_done'),
    path('reset/<uidb64>/<token>/', name='password_reset_confirm'),
    path('reset/done/', name='password_reset_complete'),
    
    
]
