from django.shortcuts import render, redirect, get_object_or_404
from .forms import PedidosForm, DetallePedidosFormSet, ImagenPedidosFormSet
from .models import Pedidos, Pedidos_imagen

# Create your views here.
def index(request):
    return render(request, 'index.html')

def pedidos(request):
    return render(request, 'pedidos.html')

def crear_pedidos(request):
    if request.method == 'POST':
      form = PedidosForm(request.POST)
      formset = DetallePedidosFormSet(request.POST)
      imagen_formset = ImagenPedidosFormSet(request.POST, request.FILES)
      if form.is_valid() and formset.is_valid():
          pedidos = form.save()
          pedidos_detalle = formset.save(commit=False)
          #print(request.POST)
          for detalle in pedidos_detalle:
              detalle.pedido = pedidos
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