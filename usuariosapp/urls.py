from django.conf.urls.static import static
from django.urls import path
from . import views

app_name= 'USUARIOS'
urlpatterns = [
    path('registro/', views.registrarse, name="registrarse")
]
