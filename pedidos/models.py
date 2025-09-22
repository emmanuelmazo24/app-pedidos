from django.contrib.auth.models import User
from django.db import models

MOLDE_CHOICES = [('MASCULINO','MASCULINO'),
                 ('FEMENINO','FEMENINO'),]

CALIDAD_CHOICES = [('ECONOMICA','ECONOMICA'),
                    ('ESTANDAR','ESTANDAR'),
                    ('PREMIUM','PREMIUM'),
                    ('SUPER PREMIUM','SUPER PREMIUM'),]

CUELLO_CHOICES = [('REDONDO','REDONDO'),
                  ('TIPO V','TIPO V')]

TIPO_USER_CHOICES = [('CLIENTE','CLIENTE'),
                    ('ADMIN','ADMIN'),
                    ('VENDEDOR','VENDEDOR'),]

INDUMENTARIA_CHOICES = [('EQUIPO COMPLETO','EQUIPO COMPLETO'),
                    ('CAMISETA SOLA','CAMISETA SOLA'),
                    ('CAMISETA Y SHORT','CAMISETA Y SHORT'),]

TALLE_CHOICES = [('PP','PP'),
                 ('S','S'),
                 ('M','M'),
                 ('L','L'),
                 ('XL','XL'),
                 ('XXL','XXL'),
                 ('3XL','3XL'),]

ESTADO_PED_CHOICES = [('PENDIENTE','PENDIENTE'),
                  ('APROBADO','APROBADO'),]

# Create your models here.
class Profile_user(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    tipo_usuario = models.CharField(max_length=15,choices=TIPO_USER_CHOICES)
    # def __str__(self):
    #     return self.user.username + ' - ' + self.tipo_usuario

class Pedidos(models.Model):
    nombre = models.CharField(max_length=100)
    contacto = models.CharField(max_length=100)
    telefono = models.CharField(max_length=15)
    descripcion = models.TextField()    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)
    estado = models.CharField(max_length=20,choices=TIPO_USER_CHOICES,default='PENDIENTE')
    total = models.FloatField(default=0)
    seña = models.FloatField(default=0)
    saldo = models.FloatField(default=0)
    fecha_entrega = models.DateField(null=True, blank=True)
    img_jugadores = models.ImageField(upload_to='imagenes_pedidos/',
        null=True,
        blank=True)
    img_arquero = models.ImageField(upload_to='imagenes_pedidos/',
        null=True,
        blank=True)
    img_auspicio1 = models.ImageField(upload_to='imagenes_pedidos/',
        null=True,
        blank=True)
    img_auspicio2 = models.ImageField(upload_to='imagenes_pedidos/',
        null=True,
        blank=True)
    img_auspicio3 = models.ImageField(upload_to='imagenes_pedidos/',
        null=True,
        blank=True)
    img_auspicio4 = models.ImageField(upload_to='imagenes_pedidos/',
        null=True,
        blank=True)
    img_auspicio5 = models.ImageField(upload_to='imagenes_pedidos/',
        null=True,
        blank=True)
    
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
    talle = models.CharField(max_length=3,choices=TALLE_CHOICES)
    dorsal = models.IntegerField(null=False)
    molde = models.CharField(max_length=15,choices=MOLDE_CHOICES)
    cuello_tipo = models.CharField(max_length=50,choices=CUELLO_CHOICES)
    cuello_color = models.CharField(max_length=15)
    observacion = models.CharField(max_length=200,blank=True)
    indumentaria = models.CharField(max_length=20,choices=INDUMENTARIA_CHOICES)
    calidad = models.CharField(max_length=20,choices=CALIDAD_CHOICES)
    cantidad = models.IntegerField(default=1)    
    precio_aprobado = models.FloatField(default=0)
    def __str__(self):
        return f"{self.nombre} - {self.talle} Talle"

class PreciosIndumentaria(models.Model):
    calidad = models.CharField(max_length=20,choices=CALIDAD_CHOICES)
    indumentaria = models.CharField(max_length=20,choices=INDUMENTARIA_CHOICES)
    precio_unitario = models.IntegerField()
    fecha_actualizacion = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
