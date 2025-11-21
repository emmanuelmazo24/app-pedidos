from django import forms
from .models import Galeria

class GaleriaForm(forms.ModelForm):
    class Meta:
        model = Galeria
        fields = ['titulo', 'descripcion', 'imagen', 'categoria', 'orden', 'activo']
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Título'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'imagen': forms.FileInput(attrs={'class': 'form-control', 'accept': 'image/*'}),
            'categoria': forms.Select(attrs={'class': 'form-control'}),
            'orden': forms.NumberInput(attrs={'class': 'form-control'}),
            'activo': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }