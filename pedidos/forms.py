from django import forms
from django.forms import ModelForm,inlineformset_factory
from .models import Pedidos, Pedidos_detalle, Pedidos_imagen, PreciosIndumentaria
from django.contrib.auth.models import User
class PedidosForm(ModelForm):
    class Meta:
        model = Pedidos
        fields = ['nombre', 'contacto', 'telefono', 'total','descripcion','img_jugadores','img_arquero','img_auspicio1','img_auspicio2','img_auspicio3','img_auspicio4','img_auspicio5']
        labels = {
        'nombre': 'Pedido',
        'contacto': 'Contacto',
        'telefono': 'Teléfono',
        'descripcion': 'Descripción',
        'total': 'Total',
        'img_jugadores': 'Diseño Jugadores',
        'img_arquero': 'Diseño Arquero',
        'img_auspicio1': 'Auspiciante 1',
        'img_auspicio2': 'Auspiciante 2',
        'img_auspicio3': 'Auspiciante 3',
        'img_auspicio4': 'Auspiciante 4',
        'img_auspicio5': 'Auspiciante 5',
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
                  }),
                  'total': forms.NumberInput(attrs={'readonly': 'readonly', 
                      'class': 'form-control'
                        }),
                  'img_jugadores': forms.ClearableFileInput(attrs={
                      'class': 'form-control',  
                      }),
                  'img_arquero': forms.ClearableFileInput(attrs={
                      'class': 'form-control',  
                      }),
                  'img_auspicio1': forms.ClearableFileInput(attrs={
                      'class': 'form-control',
                      }),
                  'img_auspicio2': forms.ClearableFileInput(attrs={
                      'class': 'form-control',
                      }),
                  'img_auspicio3': forms.ClearableFileInput(attrs={
                      'class': 'form-control',
                      }),
                  'img_auspicio4': forms.ClearableFileInput(attrs={
                      'class': 'form-control',  
                      }),
                  'img_auspicio5': forms.ClearableFileInput(attrs={
                      'class': 'form-control',
                      })
                }
    # def __init__(self, *args, **kwargs):
    #   super().__init__(*args, **kwargs)
    #   for field in self.fields.values():
    #     field.label_suffix = ''
    #     if 'class' in field.widget.attrs:
    #         field.widget.attrs['class'] += ' form-control'
    #         field.label = field.label_tag(attrs={'class': ' form-label'})
    #     else:
    #         field.widget.attrs['class'] = 'form-control'
    #         field.label = field.label_tag(attrs={'class': 'form-label'})          

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
      fields = ['id','nombre', 'talle', 'dorsal', 'molde', 'cuello_tipo', 'cuello_color', 'observacion', 'indumentaria','calidad', 'cantidad','precio_aprobado']
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
                 'precio_aprobado': forms.NumberInput(attrs={'readonly': 'readonly'}),
                 'id': forms.HiddenInput()}
        
class PreciosIndumentariaForm(ModelForm):
    class Meta:
        model = PreciosIndumentaria
        fields = ['calidad','indumentaria','precio_unitario']
        Labels = {'calidad': 'Calidad',
                  'indumentaria': 'Indumentaria',
                  'precio_unitario': 'Precio Unitario'}
        widgers = {'calidad': forms.Select(),
                    'indumentaria': forms.Select(),
                    'precio_unitario': forms.NumberInput()}

class MiCambioPasswordForm(forms.Form):
    contrasenha_actual = forms.CharField(
        label="Contraseña actual",
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )
    nueva_contrasenha = forms.CharField(
        label="Nueva contraseña",
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )
    confirmar_contrasenha = forms.CharField(
        label="Confirmar nueva contraseña",
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )

    def clean(self):
        cleaned_data = super().clean()
        nueva = cleaned_data.get("nueva_contrasenha")
        confirmar = cleaned_data.get("confirmar_contrasenha")

        if nueva and confirmar and nueva != confirmar:
            raise forms.ValidationError("Las contraseñas nuevas no coinciden.")
        return cleaned_data

class EditarPerfilForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Apellido'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Correo electrónico'}),
        }
        labels = {
            'first_name': 'Nombre',
            'last_name': 'Apellido',
            'email': 'Correo electrónico',
        }

    def clean_email(self):
        email = self.cleaned_data.get('email')
        user_qs = User.objects.filter(email=email).exclude(pk=self.instance.pk)
        if user_qs.exists():
            raise forms.ValidationError("Este correo ya está en uso por otro usuario.")
        return email   
# Inline Formset: permite manejar cabecera + detalle
DetallePedidosFormSet = inlineformset_factory(
    Pedidos,
    Pedidos_detalle,
    form=PedidosDetalleForm,
    extra=1,           # cuántos formularios vacíos aparecen
    can_delete=False    # permitir eliminar detalles
)

DetallePedidosEdFormSet = inlineformset_factory(
    Pedidos,
    Pedidos_detalle,
    form=PedidosDetalleForm,
    extra=0,           # cuántos formularios vacíos aparecen
    can_delete=True    # permitir eliminar detalles
)

ImagenPedidosFormSet = inlineformset_factory(
    Pedidos,
    Pedidos_imagen,
    form=PedidoImagenForm,
    extra=1,           # cuántos formularios vacíos aparecen
    can_delete=False    # permitir eliminar detalles
)