from django.db import models
from django.core.validators import FileExtensionValidator
# Create your models here.
class Categoria(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)
    
    def __str__(self):
        return self.nombre

class Galeria(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField(blank=True)
    imagen = models.ImageField(
        upload_to='galeria/%Y/%m/',
        validators=[FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png', 'gif'])]
    )
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name='imagenes')
    orden = models.PositiveIntegerField(default=0)
    activo = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['orden', '-fecha_creacion']
        verbose_name_plural = 'Galerías'
    
    def __str__(self):
        return self.titulo