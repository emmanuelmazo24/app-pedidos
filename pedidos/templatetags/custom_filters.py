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