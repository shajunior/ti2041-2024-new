from django.db import models

class Categoria(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Marca(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Caracteristica(models.Model):
    tipo = models.CharField(max_length=100)

    def __str__(self):
        return self.tipo

class Producto(models.Model):
    codigo = models.CharField(max_length=10)
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
    caracteristicas = models.ManyToManyField(Caracteristica, through="Enlace")

    def __str__(self):
        return f'{self.nombre} ({self.codigo})'
    
class Enlace(models.Model):
    caracteristica = models.ForeignKey(Caracteristica, null=False, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, null=False, on_delete=models.CASCADE)
