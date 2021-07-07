from django.db import models

# Create your models here.
class CateProducto (models.Model):
    nombre= models.CharField(max_length= 50)
    created =models.DateTimeField(auto_now_add=True)
    updated= models.DateTimeField(auto_now_add=True)

    class  Meta:
        
        verbose_name = 'CateProd'
        verbose_name_plural = 'CateProds'

    def __str__(self):
        return self.nombre

class Productos (models.Model):
    nombre_prod=models.CharField(max_length= 50)
    categoria= models.ForeignKey(CateProducto, on_delete= models.CASCADE)
    imagen=models.ImageField(upload_to='compra')
    precio= models.FloatField()
    disponible= models.BooleanField(default=True)
    created =models.DateTimeField(auto_now_add=True)
    updated= models.DateTimeField(auto_now_add=True)

    
    class Meta:
        
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'

