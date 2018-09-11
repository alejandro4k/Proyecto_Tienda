from django.shortcuts import render, redirect
from .forms import *
from .models import Producto
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.core import serializers

# Create your views here.
def vista_about(request):
    return render(request,'about.html')
def vista_home(request):
    return render(request,'home.html')
def vista_main(request):
    return render(request,'Examen CSS/index.html')
def vista_contacto(request):
    info_enviado=False
    email = ''
    title = ''
    text = ''
    if request.method == "POST":
        formulario=contacto_form(request.POST)
        if formulario.is_valid():
            info_enviado=True
            email= formulario.cleaned_data['correo']
            title= formulario.cleaned_data['titulo']
            text= formulario.cleaned_data['texto']
    else:
        formulario = contacto_form()
    return render(request,'contacto.html', locals())
def vista_lista_producto(request):
    lista = Producto.objects.filter()
    return render(request, 'lista_producto.html', locals())

def vista_lista_marca(request):
    listam = Marca.objects.filter()
    return render(request,'lista_marca.html', locals())
def vista_lista_categoria(request):
    listacat = Categoria.objects.filter()
    return render(request,'lista_categoria.html',locals())
def vista_eliminar_categoria(request, id_cat):
    cat = Categoria.objects.get(id = id_cat)
    cat.delete()
    return redirect('/lista_categoria/')
def vista_agregar_producto(request):
    if request.method =='POST':
        formulario = agregar_producto_form(request.POST, request.FILES)
        if formulario.is_valid():
            prod = formulario.save(commit = False)
            prod.status = True
            prod.save()
            formulario.save_m2m()
            return redirect ('/lista_producto/')
    else:
        formulario = agregar_producto_form()
    return render(request, 'vista_agregar_producto.html', locals())

def vista_agregar_marca(request):
    if request.method =='POST':
        formulario = agregar_marca_form(request.POST,request.FILES)
        if formulario.is_valid():
            marc = formulario.save(commit = False)
            marc.status=True
            marc.save()
            return redirect ('/lista_marca/')
    else:
        formulario = agregar_marca_form()
    return render (request, 'vista_agregar_marca.html', locals())

def vista_agregar_categoria(request):
    if request.method == 'POST':
        formulario = agregar_categoria_form(request.POST,request.FILES)
        if formulario.is_valid():
            form = formulario.save(commit = False)
            form.status=True
            form.save()
            return redirect('/lista_categoria/')
    else:
        formulario = agregar_categoria_form()
    return render(request,'vista_agregar_categoria.html', locals())


def vista_ver_producto(request, id_prod):
    p = Producto.objects.get( id=id_prod )
    return render(request,'ver_producto.html', locals())

def vista_editar_producto(request, id_prod):
    prod = Producto.objects.get(id = id_prod)
    if request.method == 'POST':
        formulario = agregar_producto_form(request.POST, request.FILES, instance=prod)
        if formulario.is_valid():
            prod = formulario.save()
            return redirect ('/lista_producto/')
    else:
        formulario = agregar_producto_form(instance=prod)
    return render(request, 'vista_agregar_producto.html', locals())

def vista_eliminar_producto(request, id_prod):
    prod = Producto.objects.get(id =id_prod)
    prod.delete()
    return redirect ('/lista_producto/')

def vista_eliminar_marca(request, id_marc):
    marc = Marca.objects.get(id = id_marc)
    marc.delete()
    return redirect ('/lista_marca/')

def vista_eliminar_perfil(request, id_perfil):
    perf = Perfil.objects.get(id = id_perfil)
    perf.delete()
    return redirect('/lista_perfil.html/')

def vista_login(request):
    usu=''
    cla=''
    if request.method =="POST":
        formulario = login_form(request.POST)
        if formulario.is_valid():
            usu = formulario.cleaned_data['usuario']
            cla = formulario.cleaned_data['clave']
            usuario = authenticate(username=usu, password=cla)
            if usuario is not None and usuario.is_active:
                login(request, usuario)
                return redirect('/')
            else:
                msj = "usuario o clave incorrectos"
    formulario = login_form()
    return render(request, 'login.html', locals())

def vista_logout(request):
    logout(request)
    return redirect('/login/')

def vista_inicio(request):
    return render(request, 'inicio.html')

def vista_register (request):
    formulario = register_form()
    if request.method=='POST':
        formulario = register_form(request.POST)
        if formulario.is_valid():
            usuario = formulario.cleaned_data['username']
            correo = formulario.cleaned_data['email']
            password_1 = formulario.cleaned_data['password_1']
            password_2 = formulario.cleaned_data['password_2']
            u =User.objects.create_user(username=usuario, email=correo, password=password_1)
            u.save()
            return redirect ('/login/')
        else:
            return render(request, 'register.html', locals())
    return render(request, 'register.html', locals())

def vista_crear_perfil(request):
    form_1 = register_form()
    form_2 = perfil_form()
    if request.method=='POST':
        form_1 = register_form(request.POST)
        form_2 = perfil_form(request.POST, request.FILES)
        if form_1.is_valid() and form_2.is_valid():
            usuario = form_1.cleaned_data['username']
            correo = form_1.cleaned_data['email']
            password_1 = form_1.cleaned_data['password_1']
            password_2 = form_1.cleaned_data['password_2']
            u =User.objects.create_user(username=usuario, email=correo, password=password_1)
            u.save()

            z = form_2.save(commit=False)
            z.user = u
            z.save()
    return render(request, 'perfil.html', locals())

def vista_lista_perfil(request):
    listap = Perfil.objects.filter()
    return render(request,'lista_perfil.html', locals())

def ws_productos_vista(request):
    data = serializers.serialize('xml',Producto.objects.filter(status = True))
    return HttpResponse(data, content_type='application/xml')



