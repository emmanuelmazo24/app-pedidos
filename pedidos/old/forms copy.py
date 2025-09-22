from django import forms
from django.forms import ModelForm,inlineformset_factory
from .models import Pedidos, Pedidos_detalle, Pedidos_imagen

class PedidosForm(ModelForm):
    class Meta:
        model = Pedidos
        fields = ['nombre', 'contacto', 'telefono', 'descripcion']
        labels = {
        'nombre': 'Pedido',
        'contacto': 'Contacto',
        'telefono': 'Teléfono',
        'descripcion': 'Descripción',
        }
        # help_texts = {
        #     'telefono': 'Ingrese un número de teléfono válido.',
        #     'descripcion': 'Proporcione detalles adicionales sobre el pedido.',
        # }
        # You can customize widgets here if needed
        widgets = { 'nombre': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Indique nombre o referencia del pedido'
                  }), 
                  'contacto': forms.TextInput(attrs={
                      'class': 'form-control',
                      'placeholder': 'Indique nombre del contacto'
                  }),
                  'telefono': forms.TextInput(attrs={
                      'class': 'form-control',
                      'placeholder': 'Indique el telefono del contacto'
                  }),
                  'descripcion': forms.Textarea(attrs={
                      'class': 'form-control',
                      'placeholder': 'Indique alguna descripcion del pedido',
                      'rows': 4,
                  }),}
        
class PedidoImagenForm(ModelForm):
    class Meta:
        model = Pedidos_imagen
        fields = ['imagen']

        widgets = { 'imagen': forms.ClearableFileInput(attrs={
                'class': 'form-control',  
                  }), }

class PedidosDetalleForm(ModelForm):    
    class Meta:
      model = Pedidos_detalle
      fields = ['nombre', 'talle', 'dorsal', 'molde', 'cuello_tipo', 'cuello_color', 'observacion', 'indumentaria','calidad', 'cantidad','precio_aprobado']
      labels = {
          'nombre': 'Nombre',
          'talle': 'Talle',
          'dorsal': 'Número de Dorsal',
          'molde': 'Molde',
          'cuello_tipo': 'Tipo de Cuello',
          'cuello_color': 'Color del Cuello',
          'observacion': 'Observaciones',
          'indumentaria': 'Indumentaria',
          'calidad': 'Calidad',
          'cantidad': 'Cantidad',
          'precio_aprobado': 'Precio',          
      }
      
      widgets = { 'molde': forms.Select(),
                 'talle': forms.Select(),
                 'cuello_tipo': forms.Select(),
                 'calidad': forms.Select(),
                 'indumentaria': forms.Select(),
                 'cantidad': forms.NumberInput(attrs={'readonly': 'readonly'}),
                 'precio_aprobado': forms.NumberInput(attrs={'readonly': 'readonly'})}
        

# Inline Formset: permite manejar cabecera + detalle
DetallePedidosFormSet = inlineformset_factory(
    Pedidos,
    Pedidos_detalle,
    form=PedidosDetalleForm,
    extra=1,           # cuántos formularios vacíos aparecen
    can_delete=True    # permitir eliminar detalles
)

ImagenPedidosFormSet = inlineformset_factory(
    Pedidos,
    Pedidos_imagen,
    form=PedidoImagenForm,
    extra=7,           # cuántos formularios vacíos aparecen
    can_delete=False    # permitir eliminar detalles
)