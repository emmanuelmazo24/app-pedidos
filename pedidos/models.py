from django.db import models

MOLDE_CHOICES = [('MASCULINO','MASCULINO'),
                 ('FEMENINO','FEMENINO'),]
CALIDAD_CHOICES = [('ECONOMICA','ECONOMICA'),
                    ('ESTANDAR','ESTANDAR'),
                    ('PREMIUM','PREMIUM'),]
CUELLO_CHOICES = [('REDONDO','REDONDO'),
                  ('TIPO V','TIPO V')]

# Create your models here.
class Pedidos(models.Model):
    nombre = models.CharField(max_length=100)
    contacto = models.CharField(max_length=100)
    telefono = models.CharField(max_length=15)
    descripcion = models.TextField()    
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre

class Pedidos_imagen(models.Model):
    pedido = models.ForeignKey(Pedidos, on_delete=models.CASCADE,related_name='detalles_imagen')
    imagen = models.ImageField(upload_to='imagenes_pedidos/',
        null=True,
        blank=True)
    nombre_imagen = models.CharField(max_length=255, blank=True)

    def save(self, *args, **kwargs):
        if self.imagen and not self.nombre_imagen:
            self.nombre_imagen = self.imagen.name
        super().save(*args, **kwargs)

class Pedidos_detalle(models.Model):
    pedido = models.ForeignKey(Pedidos, on_delete=models.CASCADE,related_name='detalles')
    nombre = models.CharField(max_length=100)
    talle = models.CharField(max_length=2)
    dorsal = models.IntegerField()
    molde = models.CharField(max_length=15,choices=MOLDE_CHOICES)
    cuello_tipo = models.CharField(max_length=50,choices=CUELLO_CHOICES)
    cuello_color = models.CharField(max_length=15)
    observacion = models.CharField(max_length=200,blank=True)
    calidad = models.CharField(max_length=20,choices=CALIDAD_CHOICES)
    cantidad = models.IntegerField()    

    def __str__(self):
        return f"{self.nombre} - {self.talle} Talle"
