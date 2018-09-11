from django.urls import path
from .views import *

urlpatterns =[
    path("", vista_inicio , name='vista_inicio'),
    path('about/',vista_about),
    path('home/',vista_home),
    path('main/',vista_main),
    path('contacto/',vista_contacto),
    path('lista_producto/',vista_lista_producto, name='vista_lista_producto'),
    path('lista_perfil/',vista_lista_perfil, name='vista_lista_perfil'),
    path('lista_marca/',vista_lista_marca, name='vista_lista_marca'),
    path('lista_categoria/',vista_lista_categoria, name='vista_lista_categoria'),
    path('agregar_producto/',vista_agregar_producto, name='vista_agregar_producto'),
    path('agregar_marca/',vista_agregar_marca, name='vista_agregar_marca'),
    path('agregar_categoria/',vista_agregar_categoria, name='vista_agregar_categoria'),
    path('ver_producto/<int:id_prod>/', vista_ver_producto, name='vista_ver_producto'),
    path('editar_producto/<int:id_prod>/', vista_editar_producto, name='vista_editar_producto'),
    path('eliminar_producto/<int:id_prod>/', vista_eliminar_producto, name='vista_eliminar_producto'),
    path('eliminar_marca/<int:id_marc>/', vista_eliminar_marca, name='vista_eliminar_marca'),
    path('eliminar_categoria/<int:id_cat>/', vista_eliminar_categoria, name='vista_eliminar_categoria'),
     path('eliminar_perfil/<int:id_perfil>/', vista_eliminar_perfil, name='vista_eliminar_perfil'),
    path('login/', vista_login, name='vita_login'),
    path('logout/', vista_logout, name='vista_logout'),
    path('crear_perfil/', vista_crear_perfil, name='vista_crear_perfil'),
    path('register/', vista_register, name='vista_register'),
    path('ws/productos/',ws_productos_vista, name= 'ws_productos_vista',)

]