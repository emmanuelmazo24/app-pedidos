from django.contrib import admin
from .models import Profile_user,Pedidos,PreciosIndumentaria

# Register your models here.

class Profile_fields(admin.ModelAdmin):
    list_display = ['user','tipo_usuario']

class Pedidos_fields(admin.ModelAdmin):
    list_display = ['nombre','contacto','telefono','fecha_creacion']

class PreciosIndumentaria_fields(admin.ModelAdmin):
    list_display = ['calidad','indumentaria','precio_unitario','fecha_actualizacion','user']
    

admin.site.register(Profile_user,Profile_fields)
admin.site.register(Pedidos,Pedidos_fields)
admin.site.register(PreciosIndumentaria,PreciosIndumentaria_fields)