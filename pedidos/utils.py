from .models import Profile_user

def obtener_tipo_usuario(user):
    """
    Función auxiliar para determinar el tipo de usuario.
    """
    if user.is_authenticated:
        #if hasattr(user, 'tipo_usuario'):
        return Profile_user.objects.get(user=user).tipo_usuario if Profile_user.objects.filter(user=user).exists() else 'ADMIN'
    return None