from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('pedidos/', views.crear_pedidos, name='pedidos'),
    path('crear_pedidos/', views.crear_pedidos, name='crear_pedidos'),
]