from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('signup/', views.signup, name='signup'),
    path('signin/', views.signin, name='signin'),
    path('logout/', views.signout, name='logout'),
    path('pedidos/', views.pedidos, name='pedidos'),
    path('crear_pedidos/', views.crear_pedidos, name='crear_pedidos'),
    path('pedidos_detalle/<int:pedido_id>', views.pedidos_detalle, name='pedidos_detalle'),
    path('pedidos_pdf_view/<int:pedido_id>',views.pedidos_pdf_view,name='pedidos_pdf'),
    path('obtener_precio/', views.obtener_precio, name='obtener_precio'),
]

# Solo en modo desarrollo
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)