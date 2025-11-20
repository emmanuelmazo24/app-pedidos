from django import template

register = template.Library()

@register.filter
def miles_decimal(value, decimales=2):
    try:
        value = float(value)
        # Formatea con coma para miles y punto para decimales, luego invierte
        return f"{value:,.{decimales}f}".replace(",", "X").replace(".", ",").replace("X", ".")
    except (ValueError, TypeError):
        return value

@register.filter
def get_field_value(obj, field_name):
    return getattr(obj, field_name)

@register.filter
def add_class(field, class_name):
    """Agrega una clase CSS al campo"""
    if hasattr(field.field.widget, 'attrs'):
        field.field.widget.attrs['class'] = class_name
    return field