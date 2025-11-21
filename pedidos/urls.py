from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('signup/', views.signup, name='signup'),
    path('signin/', views.signin, name='signin'),
    path('logout/', views.signout, name='logout'),
    path('pedidos/', views.pedidos, name='pedidos'),
    path('crear_pedidos/', views.crear_pedidos, name='crear_pedidos'),
    path('pedidos_detalle/<int:pedido_id>', views.pedidos_detalle, name='pedidos_detalle'),
    path('pedidos_pdf_view/<int:pedido_id>',views.pedidos_pdf_view,name='pedidos_pdf'),
    path('exportar/excel/openpyxl/<int:pedido_id>', views.exportar_detalle_excel_openpyxl, name='pedidos_xls'),
    path('pedidos_aprobar/<int:pedido_id>',views.pedidos_aprobar,name='pedidos_aprobar'),
    path('obtener_precio/', views.obtener_precio, name='obtener_precio'),
    path('precio_indumentaria/', views.precio_indumentaria, name='precio_indumentaria'),
    path('precio_indumentaria/<int:precio_id>', views.precio_indumentaria, name='precio_indumentaria_edit'),
    path('del_precio/<int:precio_id>', views.del_precio, name='del_precio'),
    path('perfil/', views.perfil, name='perfil'),
    path('editar_perfil/', views.editar_perfil, name='editar_perfil'),
    path('update_password/', views.update_password, name='update_password'),
    path('crear-superusuario/', views.crear_superusuario),  # ruta temporal    
]