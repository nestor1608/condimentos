from django.urls import path
from . import views

app_name= "carro"

urlpatterns = [
    path("agregar/<int:producto_id>/",views.Agregar_producto, name="add"),
    path("eliminar/<int:producto_id>/",views.Eliminar_producto, name="remove"),
    path("restar/<int:producto_id>/",views.Restar_producto, name="delete"),
    path("limpiar/",views.limpiar_carro, name="limpiar"),
] 