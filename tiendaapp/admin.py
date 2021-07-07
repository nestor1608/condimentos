from django.contrib import admin
from .models import CateProducto,Productos

# Register your models here.
class CategoriaAdmin(admin.ModelAdmin):
    readonly_fields=('created','updated')

class ProductosAdmin(admin.ModelAdmin):
    readonly_fields=('created','updated')

admin.site.register(CateProducto, CategoriaAdmin)
admin.site.register(Productos,ProductosAdmin)    
    
