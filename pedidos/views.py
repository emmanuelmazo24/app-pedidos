from django.shortcuts import render, redirect, get_object_or_404
from .forms import PedidosForm, PedidosDetalleForm, DetallePedidosFormSet, DetallePedidosEdFormSet
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required
from .models import Pedidos, Profile_user,Pedidos_detalle, Pedidos_imagen,PreciosIndumentaria
from xhtml2pdf import pisa
from django.template.loader import get_template
from django.http import HttpResponse, JsonResponse
from django.conf import settings
import os

# Create your views here.
def index(request):
    return render(request, 'index.html')

def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html', {"form": UserCreationForm})
    else:

        if request.POST["password1"] == request.POST["password2"]:
            try:
                user = User.objects.create_user(
                    request.POST["username"], password=request.POST["password1"])
                user.save()
                Profile_user.objects.create(
                    user=user,
                    tipo_usuario = 'CLIENTE'
                )
                login(request, user)
                return redirect('pedidos')
            except IntegrityError:
                return render(request, 'signup.html', {"form": UserCreationForm, "error": "Usuario ya existe."})

        return render(request, 'signup.html', {"form": UserCreationForm, "error": "Verifique password."})  

def signin(request):
    if request.method == 'GET':
        return render(request, 'signin.html', {"form": AuthenticationForm})
    else:
        user = authenticate(
            request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'signin.html', {"form": AuthenticationForm, "error": "Usuario o Password incorrecto."})

        login(request, user)
        return redirect('pedidos')

@login_required
def signout(request):
    logout(request)
    return redirect('index')

@login_required
def pedidos(request):
    profiles = Profile_user.objects.filter(user = request.user)

    if profiles.exists():        
        for profile in profiles:
            
            if profile.tipo_usuario == 'CLIENTE':
                pedidos = Pedidos.objects.filter(user=request.user)
            else:
                pedidos = Pedidos.objects.all()
    else:
        pedidos = Pedidos.objects.all()
    # if profile.tipo_usuario == 'CLIENTE':
    #     pedidos = Pedidos.objects.filter(user=request.user)
    # else:
    #     pedidos = Pedidos.objects.all()
    return render(request, 'pedidos.html', {'pedidos': pedidos})

@login_required
def crear_pedidos(request):
    if request.method == 'POST':
      try:
        form = PedidosForm(request.POST, request.FILES)
        formset = DetallePedidosFormSet(request.POST)
        if form.is_valid() and formset.is_valid():
            pedidos = form.save(commit=False)
            pedidos.user = request.user
            pedidos.save()
            # Guardar los detalles del pedido
            pedidosDetalle = formset.save(commit=False)
            total_aprobado = 0
            #print(request.POST)
            #un nuevo comentario
            for detalle in pedidosDetalle:
                detalle.pedido = pedidos
                precio = PreciosIndumentaria.objects.get(indumentaria=detalle.indumentaria, calidad=detalle.calidad).precio_unitario
                detalle.precio_aprobado = precio
                detalle.save()
                total_aprobado += precio
            # Guardar la suma en la cabecera del pedido
            pedidos.total = total_aprobado
            pedidos.save()
            return redirect('index')  # Redirect to a success page or another view
      except ValueError as e:
        print(f"Error al guardar el pedido: {e}")
        return render(request, 'create_pedido.html', {'form': form, 'formset': formset, 'error': 'Ocurrió un error al guardar el pedido. Por favor, intente de nuevo.'})
    else:
      form = PedidosForm()
      pedido = Pedidos()
      formset = DetallePedidosFormSet(instance=pedido)      
    return render(request, 'create_pedido.html', {'form': form, 'formset': formset})

@login_required
def pedidos_detalle(request, pedido_id):
  if request.method == 'GET':
    pedido = get_object_or_404(Pedidos, pk=pedido_id, user=request.user)   
    #pedidos_detalle = Pedidos_detalle.objects.filter(pedido=pedido)
    if pedido.estado == 'PENDIENTE':
        form = PedidosForm(instance=pedido)
        formSet = DetallePedidosEdFormSet(instance=pedido)
        return render(request, 'pedidos_detalle.html', {'form': form,'formSet': formSet, 'pedido': pedido})
    else:
        return redirect('pedidos')
  else:
    try:
        pedido = get_object_or_404(Pedidos, pk=pedido_id, user=request.user)        
        
        if request.FILES:
            form = PedidosForm(request.POST, request.FILES, instance=pedido)
        else:
            form = PedidosForm(request.POST, instance=pedido)
        total_aprobado = 0
        formset = DetallePedidosEdFormSet(request.POST, instance=pedido)
        
        # print(form.is_valid())
        # print(formset.is_valid())
        # print(formset.errors)  # Muestra los errores de cada formulario en el formset
        #print(formset.non_form_errors())  # Muestra errores generales del formset
        if form.is_valid() and formset.is_valid():            
            #print('valido')
            form.save()
            # Guardar los detalles del pedido
            pedidosDetalle = formset.save(commit=False)
            #print(pedidosDetalle)
            for detalle in pedidosDetalle:  
                #print('actualiza detalle')              
                detalle.pedido = pedido
                precio = PreciosIndumentaria.objects.get(indumentaria=detalle.indumentaria, calidad=detalle.calidad).precio_unitario
                detalle.precio_aprobado = precio
                detalle.save()                

            pedidosDetalle = Pedidos_detalle.objects.filter(pedido=pedido)
            for detalle in pedidosDetalle:
                total_aprobado += detalle.precio_aprobado
            # Eliminar los detalles marcados para eliminación         
            for detalle in formset.deleted_objects:
                #print(detalle)
                precio = PreciosIndumentaria.objects.get(indumentaria=detalle.indumentaria, calidad=detalle.calidad).precio_unitario
                detalle.delete()
                total_aprobado -= precio
            # Guardar la suma en la cabecera del pedido
            pedido.total = total_aprobado
            pedido.save()
        return redirect('pedidos')
    except ValueError:
        return render(request, 'pedidos_detalle.html', {'form': form, 'formSet': formset, 'error': 'Ocurrió un error al actualizar el pedido. Por favor, intente de nuevo.'})

def render_to_pdf(template_src, context_dict={}):
    template = get_template(template_src)
    html  = template.render(context_dict)
    response = HttpResponse(content_type='application/pdf')
    pisa_status = pisa.CreatePDF(
        html, dest=response)
    if pisa_status.err:
        return HttpResponse('Error al generar el PDF: %s' % pisa_status.err)
    return response

@login_required
def pedidos_pdf_view(request, pedido_id):
    profiles = Profile_user.objects.filter(user = request.user)
    if profiles.exists():      
        for profile_user in profiles:            
            if profile_user.tipo_usuario == 'CLIENTE':
                pedidos = get_object_or_404(Pedidos, pk=pedido_id, user=request.user)
            else:
                pedidos = get_object_or_404(Pedidos,pk=pedido_id)

        pedidos_detalle = Pedidos_detalle.objects.filter(pedido=pedidos)
        #pedidos_imagen = Pedidos_imagen.objects.filter(pedido=pedidos)  

        # for img in pedidos_imagen:
        #     img.imagen_path = os.path.join(settings.MEDIA_ROOT, os.path.basename(img.imagen.name))
        pedidos.img_jugadores_url = request.build_absolute_uri(pedidos.img_jugadores.url) if pedidos.img_jugadores else ''
        pedidos.img_arquero_url = request.build_absolute_uri(pedidos.img_arquero.url) if pedidos.img_arquero else ''
        pedidos.img_auspicio1_url = request.build_absolute_uri(pedidos.img_auspicio1.url) if pedidos.img_auspicio1 else ''
        pedidos.img_auspicio2_url = request.build_absolute_uri(pedidos.img_auspicio2.url) if pedidos.img_auspicio2 else ''
        pedidos.img_auspicio3_url = request.build_absolute_uri(pedidos.img_auspicio3.url) if pedidos.img_auspicio3 else ''
        pedidos.img_auspicio4_url = request.build_absolute_uri(pedidos.img_auspicio4.url) if pedidos.img_auspicio4 else ''
        pedidos.img_auspicio5_url = request.build_absolute_uri(pedidos.img_auspicio5.url) if pedidos.img_auspicio5 else ''

        # for img in pedidos_imagen:
        #     img.imagen_url = request.build_absolute_uri(img.imagen.url)  

        total_montos = sum([d.precio_aprobado * d.cantidad for d in pedidos_detalle])
        
        context = {
            "pedidos": pedidos,
            "pedidos_detalle": pedidos_detalle,        
            "total_montos": total_montos,
        }
    else:
        return redirect('pedidos')
        return HttpResponse('No tiene permisos para ver este pedido.')
    #return render_to_pdf('pedido_pdf_template.html', context)
    return render(request, 'pedido_pdf_template.html', context)

@login_required
def obtener_precio(request):
    indumentaria = request.GET.get('indumentaria')
    calidad = request.GET.get('calidad')
    try:
        precio = PreciosIndumentaria.objects.get(indumentaria=indumentaria, calidad=calidad).precio_unitario
    except PreciosIndumentaria.DoesNotExist:
        precio = 0
    return JsonResponse({'precio': precio})

def crear_superusuario(request):
    if User.objects.filter(username='admin').exists():
        return HttpResponse("El superusuario ya existe.")

    User.objects.create_superuser(
        username='admin',
        email='admin@example.com',
        password='admin123'  # Usa una contraseña más segura en producción
    )
    return HttpResponse("Superusuario creado.")