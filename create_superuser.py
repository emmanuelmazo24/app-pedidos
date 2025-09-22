import os
import django
from django.contrib.auth.models import User

# Configurar el entorno de Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myapp.settings')
django.setup()

# Datos del superusuario
SUPERUSER_USERNAME = os.environ.get('DJANGO_SUPERUSER_USERNAME', 'admin')
SUPERUSER_EMAIL = os.environ.get('DJANGO_SUPERUSER_EMAIL', 'admin@example.com')
SUPERUSER_PASSWORD = os.environ.get('DJANGO_SUPERUSER_PASSWORD', 'admin123')


def create_superuser():
    if not User.objects.filter(username=SUPERUSER_USERNAME).exists():
        User.objects.create_superuser(
            username=SUPERUSER_USERNAME,
            email=SUPERUSER_EMAIL,
            password=SUPERUSER_PASSWORD
        )
        print(f"Superusuario '{SUPERUSER_USERNAME}' creado exitosamente.")
    else:
        print(f"El superusuario '{SUPERUSER_USERNAME}' ya existe.")

if __name__ == '__main__':
    create_superuser()