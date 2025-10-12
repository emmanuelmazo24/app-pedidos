from .models import Profile_user
from .utils import obtener_tipo_usuario

def tipo_usuario_context(request):
    """Agrega el tipo de usuario al contexto de la plantilla."""
    #tipo_usuario = None
    tipo_usuario = obtener_tipo_usuario(request.user)
    # if request.user.is_authenticated:
    #     # Aquí defines la lógica según los campos de tu modelo de usuario
    #     if hasattr(request.user, 'tipo_usuario'):
    #         tipo_usuario = Profile_user.objects.get(user=request.user).tipo_usuario if Profile_user.objects.filter(user=request.user).exists() else 'ADMIN'
    print(tipo_usuario)
    return {'tipo_usuario': tipo_usuario}