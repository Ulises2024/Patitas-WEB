from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from django.http import JsonResponse
from .models import Producto, Categoria
from .forms import ProductoForm, RegistroUserForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login


# from .forms import ContactoForm


# Create your views here.
#PAGINA PATITAS
def index(request):
    return render(request, 'patitas.html')


#PAGINA LOGIN
def login(request):
    return render(request, 'registration/login.html')

#PAGINA NOSOTROS
def nosotros(request):
    return render(request, 'nosotros.html')

#PAGINA ADMINPAG
@login_required
def adminPage(request):
    productos = Producto.objects.all() #Realizamos una consulta y nos devuelve todos los objetos
    datosProductos = { 'productos':productos } #Creamos un diccionario para enviar como parametro la coleccion productos
    return render(request, 'adminPag.html', datosProductos)

#PAGINA DETALLE
def detalle(request):
    return render(request, 'detalleProducto.html')


#PAGINA FORMULARIO
def formulario(request):
    return render(request, 'registration/formularioReg.html')

#PAGINA MICARRITO
@login_required
def carrito(request):
    return render(request, 'miCarrito.html')

#PAGINA PRODUCTOS
def productos(request):
    productos = Producto.objects.all()
    return render(request, 'productos.html', {'productos' : productos})



#=======================================================
#==========              CRUD              =============
#=======================================================


#--------------CREAR PRODUCTO--------------------
@login_required
def crear(request):
    if request.method=="POST":
        productoform = ProductoForm(request.POST, request.FILES)
        if productoform.is_valid():  #busca si la informacion esta protegida
            productoform.save() #similar al insert crea un nuevo objeto
            return redirect('adminPage')
    
    else:
        productoform=ProductoForm()
    return render(request, 'crear.html', {'productoform':productoform})


#--------------ELIMINAR PRODUCTO--------------------
@login_required
def eliminar(request, id):
    productoEliminado = Producto.objects.get(idNumber=id) #obtiene un objeto por su id
    productoEliminado.delete()
    return redirect ('adminPage')


#--------------MODIFICAR PRODUCTO--------------------
@login_required
def modificar(request, id):
    producto = Producto.objects.get(idNumber=id)
    datos = {
        'form' : ProductoForm(instance=producto) #DEVUELVE EL OBJETO SOLICITADO DE ACUERDO A SU IDNUMBER
    }
    if request.method=='POST':
        formulario = ProductoForm(data=request.POST, instance=producto, files=request.FILES)
        if formulario.is_valid:
            formulario.save()
            return redirect('adminPage')
        datos['form'] = ProductoForm(instance=Producto.objects.get(idNumber=id))
    return render(request, 'modificar.html', datos)


#=======================================================
#==========       SELECT  PRODUCTO         =============
#=======================================================

#PAGINA DETALLE
def detalle_productos(request, id):
    producto = Producto.objects.get(id=id)
    return render(request, 'detalleProducto.html', {'producto': producto})


#=======================================================
#==========       MOSTRAR PRODUCTOS        =============
#=======================================================

def productos(request):
    productos_limitados = Producto.objects.all()[:9]
    return render(request, 'productos.html', {'productos_limitados': productos_limitados})



#=======================================================
#==========           PAGINATOR            =============
#=======================================================


def productos(request):
    productos_list = Producto.objects.all()
    
    paginator = Paginator(productos_list, 9)  # Especifica la cantidad de productos por página
    
    page_number = request.GET.get('page')  # Obtiene el número de página actual desde los parámetros de la URL
    page_obj = paginator.get_page(page_number)  # Obtiene el objeto de página correspondiente
    
    return render(request, 'productos.html', {'page_obj': page_obj})


#=======================================================
#==========             CONTACTO           =============
#=======================================================





#=======================================================
#==========          REGISTRO USER         =============
#=======================================================

def registrar(request):
    data ={                         #PARAmetro que llega al template
        'form': RegistroUserForm()
    }
    if request.method=="POST":
        formulario = RegistroUserForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()     #Crea un objeto en el backend
            user = authenticate(username=formulario.cleaned_data["username"], 
                    password=formulario.cleaned_data["password1"])
            login(request,user)
            return redirect('index')
        data["form"]=formulario
    return render(request, 'registration/formularioReg.html',data)  