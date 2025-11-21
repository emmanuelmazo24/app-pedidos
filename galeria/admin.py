from django.contrib import admin
from .models import Categoria, Galeria

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'descripcion']
    search_fields = ['nombre']

@admin.register(Galeria)
class GaleriaAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'categoria', 'orden', 'activo', 'fecha_creacion']
    list_filter = ['categoria', 'activo', 'fecha_creacion']
    search_fields = ['titulo', 'descripcion']
    list_editable = ['orden', 'activo']
    ordering = ['orden', '-fecha_creacion']
    
    fieldsets = (
        ('Información', {
            'fields': ('titulo', 'descripcion', 'categoria')
        }),
        ('Imagen', {
            'fields': ('imagen',)
        }),
        ('Configuración', {
            'fields': ('orden', 'activo')
        }),
        ('Metadata', {
            'fields': ('fecha_creacion',),
            'classes': ('collapse',)
        }),
    )
    readonly_fields = ['fecha_creacion']