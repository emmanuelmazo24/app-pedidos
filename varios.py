        # You can customize widgets here if needed
        # widgets = { ... }
# You can create additional forms or customize existing ones as needed
# For example, if you want to create a form for searching or filtering orders, you can do that here as well.
# Remember to import and use these forms in your views as necessary.
# Example:
# from .forms import PedidosForm, PedidosDetalleForm
# def some_view(request):
#     if request.method == 'POST':
#         form = PedidosForm(request.POST)
#         if form.is_valid():
#             form.save()
#     else:
#         form = PedidosForm()
#     return render(request, 'some_template.html', {'form': form})
# This is a basic structure; you can expand upon it based on your application's requirements.
# Make sure to handle form validation, error messages, and user feedback in your views and templates.
# Also, consider using Django's built-in form features like formsets if you need to handle multiple forms on a single page.
# Additionally, you might want to implement custom validation logic within the form classes if your application requires it.
# For example:
# def clean_<fieldname>(self):
#     # Custom validation logic
#     return self.cleaned_data['<fieldname>']
# Finally, ensure that you have the necessary imports and configurations in your Django project to utilize these forms effectively.
# For example, make sure to include the app in INSTALLED_APPS in settings.py and set up URLs and views accordingly.
# This is a foundational setup; feel free to modify and enhance it as per your project's needs.
# Example of a custom validation method within the PedidosForm
# def clean_telefono(self):
#     telefono = self.cleaned_data.get('telefono')
#     if not telefono.isdigit():
#         raise forms.ValidationError("El teléfono debe contener solo números.")
#     return telefono
# Example of using a formset for Pedidos_detalle if you want to handle multiple details at once
# from django.forms import modelformset_factory
# PedidosDetalleFormSet = modelformset_factory(Pedidos_detalle, form=PedidosDetalleForm, extra=1)
# In your views, you can then use this formset to manage multiple Pedidos_detalle instances.
# Remember to import necessary modules and handle form rendering in your templates.
# This code provides a starting point for creating and managing forms related to the Pedidos and Pedidos_detalle models.
# Make sure to test the forms thoroughly to ensure they meet your application's requirements.
# You can also add help texts, labels, and error messages to enhance user experience.
# Example of adding help texts and labels
# class Meta:
#     model = Pedidos
#     fields = ['nombre', 'contacto', 'telefono', 'descripcion']
#     labels = {
#         'nombre': 'Nombre del Cliente',
#         'contacto': 'Información de Contacto',
#         'telefono': 'Número de Teléfono',
#         'descripcion': 'Descripción del Pedido',
#     }
#     help_texts = {
#         'telefono': 'Ingrese un número de teléfono válido.',
#         'descripcion': 'Proporcione detalles adicionales sobre el pedido.',
#     }
# This will help users understand what information is required when filling out the forms.
# You can customize the widgets for each field if needed
# For example, using a Textarea for the descripcion field   
# widgets = {
#     'descripcion': forms.Textarea(attrs={'rows': 4, 'cols': 40}),
# }
# This will provide a larger text area for users to enter detailed descriptions.
# Similarly, you can customize widgets for other fields as per your requirements.
# Remember to import forms from django if you are using custom widgets or validation
# from django import forms
# from django.forms import ModelForm
# from .models import Pedidos, Pedidos_detalle
# from django.forms import modelformset_factory
# from django.forms import inlineformset_factory
# PedidosDetalleFormSet = modelformset_factory(Pedidos_detalle, form=PedidosDetalleForm, extra=1)
# PedidosDetalleInlineFormSet = inlineformset_factory(Pedidos, Pedidos_detalle, form=PedidosDetalleForm, extra=1)
# # This allows you to create and manage multiple Pedidos_detalle instances related to a single Ped
# # ido instance in your views.
# idos instance in your views.
# Example usage in a view:
# def manage_pedidos(request, pedido_id):
#     pedido = get_object_or_404(Pedidos, id=pedido_id)
#     if request.method == 'POST':
#         form = PedidosForm(request.POST, instance=pedido)
#         formset = PedidosDetalleInlineFormSet(request.POST, instance=pedido)
#         if form.is_valid() and formset.is_valid():
#             form.save()
#             formset.save()
#             return redirect('some_view_name')
#     else:
#         form = PedidosForm(instance=pedido)
#         formset = PedidosDetalleInlineFormSet(instance=pedido)
#     return render(request, 'manage_pedidos.html', {'form': form, 'formset': formset})
# This setup provides a comprehensive way to handle forms for both Pedidos and its related Pedidos_detalle instances.
# Example usage in a view:
# def manage_pedidos(request, pedido_id):
#     pedido = get_object_or_404(Pedidos, id=pedido_id)
#     if request.method == 'POST':
#         form = PedidosForm(request.POST, instance=pedido)
#         formset = PedidosDetalleInlineFormSet(request.POST, instance=pedido)
#         if form.is_valid() and formset.is_valid():
#             form.save()
#             formset.save()
#             return redirect('some_view_name')
#     else:
#         form = PedidosForm(instance=pedido)
#         formset = PedidosDetalleInlineFormSet(instance=pedido)
#     return render(request, 'manage_pedidos.html', {'form': form, '
# formset': formset})
# This setup provides a comprehensive way to handle forms for both Pedidos and its related Pedidos_detalle instances.
# Make sure to create the corresponding template (manage_pedidos.html) to render the form
# and formset appropriately.
# You can use Django's form rendering capabilities to display the forms in your template.
# Example snippet for manage_pedidos.html
# <form method="post">
#     {% csrf_token %}
#     {{ form.as_p }}
#     {{ formset.management_form }}
#     {% for form in formset %}
#         {{ form.as_p }}
#     {% endfor %}
#     <button type="submit">Save</button>
# </form>
# This will render the main form and the inline formset for Pedidos_detalle.
# Make sure to handle form validation, error messages, and user feedback in your views and templates.
# Also, consider using Django's built-in form features like formsets if you need to handle
# multiple forms on a single page.
# Additionally, you might want to implement custom validation logic within the form classes if your application requires it.
# For example:
# def clean_<fieldname>(self):
#     # Custom validation logic
#     return self.cleaned_data['<fieldname>']
# Finally, ensure that you have the necessary imports and configurations in your Django project to utilize these forms effectively.
# For example, make sure to include the app in INSTALLED_APPS in settings.py and
# set up URLs and views accordingly.
# This is a foundational setup; feel free to modify and enhance it as per your project's needs.
# Example of a custom validation method within the PedidosForm
# def clean_telefono(self):
#     telefono = self.cleaned_data.get('telefono')
#     if not telefono.isdigit():
#         raise forms.ValidationError("El teléfono debe contener solo números.")
#     return telefono
# Example of using a formset for Pedidos_detalle if you want to handle multiple details at once
# from django.forms import modelformset_factory
# PedidosDetalleFormSet = modelformset_factory(Pedidos_detalle, form
# , extra=1)
# In your views, you can then use this formset to manage multiple Pedidos_detalle instances.
# Remember to import necessary modules and handle form rendering in your templates.
# This code provides a starting point for creating and managing forms related to the Pedidos and Pedidos_detalle models.
# Make sure to test the forms thoroughly to ensure they meet your application's requirements.
# You can also add help texts, labels, and error messages to enhance user experience.
# Example of adding help texts and labels
# class Meta:
#     model = Pedidos
#     fields = ['nombre', 'contacto', 'telefono', 'descripcion']
#     labels = {
#         'nombre': 'Nombre del Cliente',
#         'contacto': 'Información de Contacto',
#         'telefono': 'Número de Teléfono',
#         'descripcion': 'Descripción del Pedido',
#     }
#     help_texts = {
#         'telefono': 'Ingrese un número de teléfono válido.',
#         'descripcion': 'Proporcione detalles adicionales sobre el pedido.',
#     }
# This will help users understand what information is required when filling out the forms.
# You can customize the widgets for each field if needed
# For example, using a Textarea for the descripcion field
# widgets = {
#     'descripcion': forms.Textarea(attrs={'rows': 4, 'cols': 40}),
# }
# This will provide a larger text area for users to enter detailed descriptions.
# Similarly, you can customize widgets for other fields as per your requirements.
# Remember to import forms from django if you are using custom widgets or validation
# from django import forms
# from django.forms import ModelForm
# from .models import Pedidos, Pedidos_detalle
# from django.forms import modelformset_factory
# from django.forms import inlineformset_factory
# PedidosDetalleFormSet = modelformset_factory(Pedidos_detalle, form=PedidosDetalleForm, extra=1)
# PedidosDetalleInlineFormSet = inlineformset_factory(Pedidos, Pedidos_detalle, form=PedidosDetalleForm, extra=1)
# # This allows you to create and manage multiple Pedidos_detalle instances related to a single Ped
# # ido instance in your views.
# idos instance in your views.
# Example usage in a view:
# def manage_pedidos(request, pedido_id):
#     pedido = get_object_or_404(Pedidos, id=pedido_id)
#     if request.method == 'POST':
#         form = PedidosForm(request.POST, instance=pedido)
#         formset = PedidosDetalleInlineFormSet(request.POST, instance=pedido)
#         if form.is_valid() and formset.is_valid():
#             form.save()
#             formset.save()
#             return redirect('some_view_name')
#     else:
#         form = PedidosForm(instance=pedido)
#         formset = PedidosDetalleInlineFormSet(instance=pedido)
#     return render(request, 'manage_pedidos.html', {'form': form, 'formset': formset})
# This setup provides a comprehensive way to handle forms for both Pedidos and its related Pedidos
# detalle instances.
# Example usage in a view:
# def manage_pedidos(request, pedido_id):
#     pedido = get_object_or_404(Pedidos, id=pedido_id)
#     if request.method == 'POST':
#         form = PedidosForm(request.POST, instance=pedido)
#         formset = PedidosDetalleInlineFormSet(request.POST, instance=pedido)
#         if form.is_valid() and formset.is_valid():
#             form.save()
#             formset.save()
#             return redirect('some_view_name')
#     else:
#         form = PedidosForm(instance=pedido)
#         formset = PedidosDetalleInlineFormSet(instance=pedido)
#     return render(request, 'manage_pedidos.html', {'form': form, '
# formset': formset})
# This setup provides a comprehensive way to handle forms for both Pedidos and its related Pedidos
# detalle instances.
# Make sure to create the corresponding template (manage_pedidos.html) to render the form
# and formset appropriately.
# You can use Django's form rendering capabilities to display the forms in your template.
# Example snippet for manage_pedidos.html
# <form method="post">
#     {% csrf_token %}
#     {{ form.as_p }}
#     {{ formset.management_form }}
#     {% for form in formset %}
#         {{ form.as_p }}
#     {% endfor %}
#     <button type="submit">Save</button>
# </form>
# This will render the main form and the inline formset for Pedidos_detalle.
# Make sure to handle form validation, error messages, and user feedback in your views and templates.
# Also, consider using Django's built-in form features like formsets if you need to handle
# multiple forms on a single page.
# Additionally, you might want to implement custom validation logic within the form classes if your application requires it.
# For example:
# def clean_<fieldname>(self):
#     # Custom validation logic
#     return self.cleaned_data['<fieldname>']
# Finally, ensure that you have the necessary imports and configurations in your Django project to utilize these forms effectively.
# For example, make sure to include the app in INSTALLED_APPS in settings.py and
# set up URLs and views accordingly.
# This is a foundational setup; feel free to modify and enhance it as per your project's needs
# Example of a custom validation method within the PedidosForm
# def clean_telefono(self):
#     telefono = self.cleaned_data.get('telefono')
#     if not telefono.isdigit():
#         raise forms.ValidationError("El teléfono debe contener solo números.")
#     return telefono
# Example of using a formset for Pedidos_detalle if you want to handle multiple details
# at once
# Perfecto, si deseas crear un campo en tu modelo para guardar el nombre de una imagen que se carga, puedes hacerlo de dos formas:

# ✅ OPCIÓN 1: Usar ImageField (lo más común y correcto)

# Esto guarda la imagen en el sistema de archivos y el nombre de la imagen (con su ruta) en la base de datos.

# En tu modelo (models.py):
# from django.db import models

# class Pedidos_detalle(models.Model):
#     # otros campos...
#     imagen = models.ImageField(
#         upload_to='imagenes_pedidos/',
#         null=True,
#         blank=True
#     )


# upload_to='imagenes_pedidos/': guarda las imágenes en MEDIA_ROOT/imagenes_pedidos/

# null=True, blank=True: para que no sea obligatorio

# En tu formulario (forms.py):

# Django renderiza automáticamente un campo de tipo archivo para ImageField.

# Pero puedes personalizarlo así:

# widgets = {
#     'imagen': forms.ClearableFileInput(attrs={'class': 'form-control'}),
# }

# En tu plantilla (.html):

# No olvides agregar esto para que el formulario pueda subir archivos:

# <form method="post" enctype="multipart/form-data">
#     {% csrf_token %}
#     {{ form.as_p }}
#     <button type="submit">Guardar</button>
# </form>

# ✅ OPCIÓN 2: Si solo quieres guardar el nombre del archivo, no la imagen (no recomendable, pero posible)

# Podrías usar un campo de texto:

# nombre_imagen = models.CharField(max_length=255, null=True, blank=True)


# Luego deberías escribir lógica para extraer el nombre del archivo cuando se sube desde un formulario. Ejemplo en la vista:

# if request.method == 'POST':
#     form = PedidosDetalleForm(request.POST, request.FILES)
#     if form.is_valid():
#         instance = form.save(commit=False)
#         if 'imagen' in request.FILES:
#             instance.nombre_imagen = request.FILES['imagen'].name
#         instance.save()


# Pero sinceramente, es más limpio usar ImageField, porque:

# Guarda automáticamente el nombre del archivo

# Valida que sea una imagen

# Puedes acceder al nombre con obj.imagen.name

# ✅ Cómo obtener solo el nombre del archivo de un ImageField:

# Supón que tienes esto en el modelo:

# imagen = models.ImageField(upload_to='imagenes_pedidos/')


# Entonces, en Python:

# nombre_archivo = obj.imagen.name            # 'imagenes_pedidos/imagen1.jpg'
# solo_nombre = obj.imagen.name.split('/')[-1]  # 'imagen1.jpg'

# ✅ Estructura recomendada: Crear un modelo separado para imágenes
# 📁 models.py
# from django.db import models

# class Pedidos_detalle(models.Model):
#     nombre = models.CharField(max_length=100)
#     # otros campos...

# class ImagenPedido(models.Model):
#     pedido_detalle = models.ForeignKey(Pedidos_detalle, on_delete=models.CASCADE, related_name='imagenes')
#     imagen = models.ImageField(upload_to='imagenes_pedidos/')
#     nombre_imagen = models.CharField(max_length=255, blank=True)

#     def save(self, *args, **kwargs):
#         if self.imagen and not self.nombre_imagen:
#             self.nombre_imagen = self.imagen.name
#         super().save(*args, **kwargs)


# Se crea una relación uno-a-muchos: un Pedidos_detalle puede tener muchas imágenes.

# El campo nombre_imagen guarda automáticamente el nombre del archivo.

# ✅ forms.py

# Puedes crear un formulario para el modelo ImagenPedido, y permitir múltiples archivos:

# from django import forms
# from .models import ImagenPedido

# class ImagenPedidoForm(forms.ModelForm):
#     class Meta:
#         model = ImagenPedido
#         fields = ['imagen']

#     imagen = forms.ImageField(
#         widget=forms.ClearableFileInput(attrs={'multiple': True}),
#         required=False
#     )

# ✅ views.py (ejemplo de vista para crear imágenes asociadas)
# def crear_pedido_con_imagenes(request):
#     if request.method == 'POST':
#         pedido_form = PedidosDetalleForm(request.POST)
#         imagen_form = ImagenPedidoForm(request.POST, request.FILES)

#         if pedido_form.is_valid():
#             pedido = pedido_form.save()

#             # Procesar múltiples imágenes
#             for archivo in request.FILES.getlist('imagen'):
#                 ImagenPedido.objects.create(pedido_detalle=pedido, imagen=archivo)

#             return redirect('detalle_pedido', pk=pedido.pk)

#     else:
#         pedido_form = PedidosDetalleForm()
#         imagen_form = ImagenPedidoForm()

#     return render(request, 'pedidos/crear.html', {
#         'pedido_form': pedido_form,
#         'imagen_form': imagen_form,
#     })

# ✅ En tu plantilla (crear.html)
# <form method="post" enctype="multipart/form-data">
#     {% csrf_token %}
#     {{ pedido_form.as_p }}
#     <label for="id_imagen">Imágenes:</label>
#     {{ imagen_form.imagen }}
#     <button type="submit">Guardar</button>
# </form>

# ✅ En el admin.py (opcional)

# Si usas el admin y quieres ver o cargar imágenes relacionadas:

# from django.contrib import admin
# from .models import Pedidos_detalle, ImagenPedido

# class ImagenPedidoInline(admin.TabularInline):
#     model = ImagenPedido
#     extra = 1

# class PedidosDetalleAdmin(admin.ModelAdmin):
#     inlines = [ImagenPedidoInline]

# admin.site.register(Pedidos_detalle, PedidosDetalleAdmin)


# @login_required
# def pedidos_pdf_view(request, pedido_id):
#     pedidos = get_object_or_404(Pedidos, pk=pedido_id)
#     pedidos_detalle = Pedidos_detalle.objects.filter(pedido=pedidos)
#     pedidos_imagen = Pedidos_imagen.objects.filter(pedido=pedidos)

#     # Traer el precio según calidad e indumentaria para cada detalle
#     for detalle in pedidos_detalle:
#         try:
#             precio_obj = PrecioIndumentaria.objects.get(
#                 calidad=detalle.calidad,
#                 indumentaria=detalle.indumentaria
#             )
#             detalle.precio_aprobado = precio_obj.precio
#         except PrecioIndumentaria.DoesNotExist:
#             detalle.precio_aprobado = 0  # O el valor que desees por defecto

#     total_montos = sum([d.precio_aprobado * d.cantidad for d in pedidos_detalle])

#     for img in pedidos_imagen:
#         img.imagen_url = request.build_absolute_uri(img.imagen.url)

#     context = {
#         "pedidos": pedidos,
#         "pedidos_detalle": pedidos_detalle,
#         "pedidos_imagen": pedidos_imagen,
#         "total_montos": total_montos,
#     }
#     return render_to_pdf('pedido_pdf_template.html', context)



# models.py

# from django.db import models

# class Factura(models.Model):
#     cliente = models.CharField(max_length=100)
#     fecha = models.DateField()
#     total = models.DecimalField(max_digits=10, decimal_places=2)

# class LineaFactura(models.Model):
#     factura = models.ForeignKey(Factura, related_name='lineas', on_delete=models.CASCADE)
#     producto = models.CharField(max_length=100)
#     cantidad = models.IntegerField()
#     precio = models.DecimalField(max_digits=10, decimal_places=2)
# 🧾 Formulario HTML (ejemplo simplificado)
# Tu formulario HTML enviaría los datos de la cabecera y las líneas así:

# html
# Copiar código
# <form method="post">
#   {% csrf_token %}

#   <!-- Cabecera -->
#   <input type="text" name="cliente" value="{{ factura.cliente }}">
#   <input type="date" name="fecha" value="{{ factura.fecha }}">
#   <input type="text" name="total" value="{{ factura.total }}">

#   <!-- Detalle (líneas) -->
#   {% for linea in factura.lineas.all %}
#     <input type="hidden" name="linea_id" value="{{ linea.id }}">
#     <input type="text" name="producto" value="{{ linea.producto }}">
#     <input type="number" name="cantidad" value="{{ linea.cantidad }}">
#     <input type="text" name="precio" value="{{ linea.precio }}">
#   {% endfor %}

#   <!-- Puedes agregar campos vacíos para nuevas líneas también -->

#   <button type="submit">Actualizar</button>
# </form>
# Pero como eso se vuelve complejo, es mejor que los inputs del detalle se nombren como listas:

# html
# Copiar código
# <input type="hidden" name="linea_id[]" value="1">
# <input type="text" name="producto[]" value="Producto 1">
# <input type="number" name="cantidad[]" value="2">
# <input type="text" name="precio[]" value="10.00">
# Así puedes manejar múltiples líneas en el backend.

# 🧠 Vista basada en función (views.py)
# python
# Copiar código
# from django.shortcuts import render, get_object_or_404, redirect
# from .models import Factura, LineaFactura
# from django.views.decorators.csrf import csrf_exempt  # solo para pruebas (no en producción)

# @csrf_exempt  # elimina esto en producción, usa {% csrf_token %} en el template
# def actualizar_factura(request, factura_id):
#     factura = get_object_or_404(Factura, id=factura_id)

#     if request.method == 'POST':
#         # 1. Actualizar cabecera
#         factura.cliente = request.POST.get('cliente')
#         factura.fecha = request.POST.get('fecha')
#         factura.total = request.POST.get('total')
#         factura.save()

#         # 2. Leer datos del detalle
#         ids = request.POST.getlist('linea_id[]')         # IDs existentes (pueden venir vacíos)
#         productos = request.POST.getlist('producto[]')   # Lista de productos
#         cantidades = request.POST.getlist('cantidad[]')
#         precios = request.POST.getlist('precio[]')

#         lineas_actualizadas = []

#         for i in range(len(productos)):
#             linea_id = ids[i] if i < len(ids) else None
#             producto = productos[i]
#             cantidad = cantidades[i]
#             precio = precios[i]

#             if linea_id:
#                 # Línea existente: actualizar
#                 try:
#                     linea = LineaFactura.objects.get(id=linea_id, factura=factura)
#                     linea.producto = producto
#                     linea.cantidad = cantidad
#                     linea.precio = precio
#                     linea.save()
#                     lineas_actualizadas.append(linea.id)
#                 except LineaFactura.DoesNotExist:
#                     continue
#             else:
#                 # Nueva línea
#                 nueva = LineaFactura.objects.create(
#                     factura=factura,
#                     producto=producto,
#                     cantidad=cantidad,
#                     precio=precio
#                 )
#                 lineas_actualizadas.append(nueva.id)

#         # 3. Eliminar líneas que ya no están
#         for linea in factura.lineas.all():
#             if linea.id not in lineas_actualizadas:
#                 linea.delete()

#         return redirect('factura_detalle', factura_id=factura.id)  # o donde quieras redirigir

#     # Si GET, renderizas el formulario con datos actuales
#     return render(request, 'factura_form.html', {'factura': factura})