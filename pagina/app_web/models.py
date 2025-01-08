from django.db import models

# Create your models here.
from django.db import models

class Producto(models.Model):
    codigo = models.CharField(max_length=10)
    producto = models.CharField(max_length=100)
    descripcion = models.TextField()
    cantidad = models.IntegerField()

    def __str__(self):
        return self.producto
