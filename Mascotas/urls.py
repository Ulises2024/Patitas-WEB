from django.urls import path
from .views import index, login, nosotros, adminPage, detalle, formulario, carrito, productos, crear, eliminar, modificar



urlpatterns = [
    path('', index, name="index"),
    path('login/', login, name="login"),
    path('nosotros/', nosotros, name="nosotros"),
    path('adminPage/', adminPage, name="adminPage"),
    path('detalle/id', detalle, name="detalle"),
    path('formulario/', formulario, name="formulario"),
    path('carrito/', carrito, name="carrito"),
    path('productos/', productos, name="productos"),
    path('crear/', crear, name="crear"),
    path('eliminar/<id>', eliminar, name="eliminar"),
    path('modificar/<id>', modificar, name="modificar"),

]


