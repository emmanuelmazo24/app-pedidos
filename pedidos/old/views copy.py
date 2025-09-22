from django.shortcuts import render, redirect, get_object_or_404
from .forms import PedidosForm, DetallePedidosFormSet, ImagenPedidosFormSet
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
      form = PedidosForm(request.POST)
      formset = DetallePedidosFormSet(request.POST)
      imagen_formset = ImagenPedidosFormSet(request.POST, request.FILES)
      if form.is_valid() and formset.is_valid():
          pedidos = form.save(commit=False)
          pedidos.user = request.user
          pedidos.save()
          # Guardar los detalles del pedido
          pedidos_detalle = formset.save(commit=False)
          #print(request.POST)
          for detalle in pedidos_detalle:
              detalle.pedido = pedidos
              precio = PreciosIndumentaria.objects.get(indumentaria=detalle.indumentaria, calidad=detalle.calidad).precio_unitario
              print(precio)
              detalle.precio_aprobado = precio
              detalle.save()
          #print(request.FILES)
          # Procesar múltiples imágenes
          if request.FILES:
            if imagen_formset.is_valid():
              for instance in imagen_formset.save(commit=False):
                instance.pedido = pedidos
                #instance.nombre_imagen = request.FILES['imagen'].name
                instance.save()

          """ for archivo in request.FILES.getlist('imagen'):
              Pedidos_imagen.objects.create(pedido=pedido, imagen=archivo)
              Pedidos_imagen.save() """

          return redirect('index')  # Redirect to a success page or another view
    else:
      form = PedidosForm()
      pedido = Pedidos()
      formset = DetallePedidosFormSet(instance=pedido)
      imagen_formset = ImagenPedidosFormSet(instance=pedido)
    #return render(request, 'create_pedido.html', {'form': form, 'formset': formset})
    return render(request, 'create_pedido.html', {'form': form, 'formset': formset, 'imagen_formset': imagen_formset})

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
    pedidos = get_object_or_404(Pedidos,pk=pedido_id)
    pedidos_detalle = Pedidos_detalle.objects.filter(pedido=pedidos)
    pedidos_imagen = Pedidos_imagen.objects.filter(pedido=pedidos)  

    # for img in pedidos_imagen:
    #     img.imagen_path = os.path.join(settings.MEDIA_ROOT, os.path.basename(img.imagen.name))

    for img in pedidos_imagen:
        img.imagen_url = request.build_absolute_uri(img.imagen.url)  

    total_montos = sum([d.precio_aprobado * d.cantidad for d in pedidos_detalle])
    
    context = {
        "pedidos": pedidos,
        "pedidos_detalle": pedidos_detalle,
        "pedidos_imagen":pedidos_imagen,
        "total_montos": total_montos,
    }
    return render_to_pdf('pedido_pdf_template.html', context)
    #return render(request, 'pedido_pdf_template.html', context)

@login_required
def obtener_precio(request):
    indumentaria = request.GET.get('indumentaria')
    calidad = request.GET.get('calidad')
    try:
        precio = PreciosIndumentaria.objects.get(indumentaria=indumentaria, calidad=calidad).precio_unitario
    except PreciosIndumentaria.DoesNotExist:
        precio = 0
    return JsonResponse({'precio': precio})