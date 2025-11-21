from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .models import Galeria, Categoria
from .forms import GaleriaForm

# Vista pública - Mostrar carrusel
def galeria_carrusel(request, categoria_id=None):
    """Muestra el carrusel de imágenes"""
    
    if categoria_id:
        categoria = get_object_or_404(Categoria, id=categoria_id)
        imagenes = Galeria.objects.filter(
            categoria=categoria, 
            activo=True
        ).order_by('orden')
        categorias = Categoria.objects.all()
        return render(request, 'galeria/carrusel.html', {
            'imagenes': imagenes,
            'categoria_actual': categoria,
            'categorias': categorias
        })
    else:
        imagenes = Galeria.objects.filter(activo=True).order_by('orden')
        categorias = Categoria.objects.all()
        return render(request, 'galeria/carrusel.html', {
            'imagenes': imagenes,
            'categorias': categorias
        })

# API para carrusel dinámico
def api_galeria_images(request, categoria_id=None):
    """API que retorna las imágenes en JSON"""
    
    if categoria_id:
        imagenes = Galeria.objects.filter(
            categoria_id=categoria_id,
            activo=True
        ).order_by('orden')
    else:
        imagenes = Galeria.objects.filter(activo=True).order_by('orden')
    
    data = [{
        'id': img.id,
        'titulo': img.titulo,
        'descripcion': img.descripcion,
        'imagen_url': img.imagen.url,
        'categoria': img.categoria.nombre
    } for img in imagenes]
    
    return JsonResponse({'imagenes': data})

# Administración de galería
@login_required
def galeria_admin_list(request):
    """Lista todas las imágenes para administrar"""
    imagenes = Galeria.objects.all().order_by('-fecha_creacion')
    categorias = Categoria.objects.all()
    
    # Filtrar por categoría si se especifica
    categoria_id = request.GET.get('categoria')
    if categoria_id:
        imagenes = imagenes.filter(categoria_id=categoria_id)
    
    return render(request, 'galeria/admin_list.html', {
        'imagenes': imagenes,
        'categorias': categorias
    })

@login_required
def galeria_admin_create(request):
    """Crear nueva imagen"""
    if request.method == 'POST':
        form = GaleriaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('galeria_admin_list')
    else:
        form = GaleriaForm()
    
    return render(request, 'galeria/admin_form.html', {'form': form, 'titulo': 'Nueva Imagen'})

@login_required
def galeria_admin_edit(request, id):
    """Editar imagen existente"""
    imagen = get_object_or_404(Galeria, id=id)
    
    if request.method == 'POST':
        form = GaleriaForm(request.POST, request.FILES, instance=imagen)
        if form.is_valid():
            form.save()
            return redirect('galeria_admin_list')
    else:
        form = GaleriaForm(instance=imagen)
    
    return render(request, 'galeria/admin_form.html', {
        'form': form,
        'titulo': f'Editar: {imagen.titulo}',
        'imagen': imagen
    })

@login_required
def galeria_admin_delete(request, id):
    """Eliminar imagen"""
    imagen = get_object_or_404(Galeria, id=id)
    
    if request.method == 'POST':
        imagen.delete()
        return redirect('galeria_admin_list')
    
    return render(request, 'galeria/admin_confirm_delete.html', {'imagen': imagen})
