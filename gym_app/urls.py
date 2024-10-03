from django.urls import path
from . import views

urlpatterns = [
    path('agregar_cliente/', views.agregar_cliente, name='agregar_cliente'),
    path('listar_clientes/', views.listar_clientes, name='listar_clientes'),  # Esta línea debe estar presente
    path('editar_cliente/<int:cliente_id>/', views.editar_cliente, name='editar_cliente'),
    path('eliminar_cliente/<int:cliente_id>/', views.eliminar_cliente, name='eliminar_cliente'),
    path('agregar_pago/', views.agregar_pago, name='agregar_pago'),
    path('agregar_gasto/', views.agregar_gasto, name='agregar_gasto'),
    path('balance_mensual/', views.balance_mensual, name='balance_mensual'),
]
