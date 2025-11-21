from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # Público
    path('carrusel/', views.galeria_carrusel, name='galeria_carrusel'),
    path('carrusel/<int:categoria_id>/', views.galeria_carrusel, name='galeria_carrusel_categoria'),
    path('api/imagenes/', views.api_galeria_images, name='api_galeria_images'),
    path('api/imagenes/<int:categoria_id>/', views.api_galeria_images, name='api_galeria_images_categoria'),
    
    # Administración
    path('admin/', views.galeria_admin_list, name='galeria_admin_list'),
    path('admin/crear/', views.galeria_admin_create, name='galeria_admin_create'),
    path('admin/editar/<int:id>/', views.galeria_admin_edit, name='galeria_admin_edit'),
    path('admin/eliminar/<int:id>/', views.galeria_admin_delete, name='galeria_admin_delete'),
]

# Solo en modo desarrollo
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)