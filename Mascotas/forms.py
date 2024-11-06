from django import forms
from django.forms import ModelForm
from django.forms import widgets
from django.forms.models import ModelChoiceField
from .models import Producto, Contacto, RegistroUserForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto    #Nombre de la clase
        fields = ['idNumber', 'nombre', 'marca', 'precio', 'descripcion', 'cantidad', 'direccion', 'categoria', 'imagen']   #Atributos de la clase
        labels = {          
            'idNumber':'Id',
            'nombre': 'Nombre',
            'marca': 'Marca', 
            'precio': 'Precio', 
            'descripcion': 'Descripción', 
            'cantidad' : 'Cantidad', 
            'direccion': 'Dirección', 
            'categoria': 'Categoria',
            'imagen': 'Imagen',
            
        }
        widgets = {
            'idNumber' : forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Ingrese Id..',
                    'id':'idNumber', 
                }
            ),
            'nombre' : forms.TextInput(
                attrs={
                    'class' : 'form-control',
                    'placeholder' : 'Ingrese nombre..',
                    'id':'nombre', 
                }
            ),
            'marca' : forms.TextInput(
                attrs={
                    'class' : 'form-control',
                    'placeholder' : 'Ingrese marca..',
                    'id':'marca', 
                }
            ),
            'precio': forms.NumberInput(
                attrs={'min': '0', 
                    'class': 'form-control',
                    'placeholder': 'Ingrese precio..',
                    'id': 'precio',
                }
            ),
            'descripcion' : forms.TextInput(
                attrs={
                    'class' : 'form-control',
                    'placeholder' : 'Ingrese descripción..',
                    'id':'descripción', 
                }
            ),
            'cantidad': forms.NumberInput(
                attrs={'min': '0', 
                    'class': 'form-control',
                    'placeholder': 'Ingrese cantidad..',
                    'id': 'cantidad',
                }
            ),
            'direccion' : forms.TextInput(
                attrs={
                    'class' : 'form-control',
                    'placeholder' : 'Ingrese dirección..',
                    'id':'dirección', 
                }
            ),
            'categoria' : forms.Select(
                attrs={
                    'class' : 'form-control',
                    'id':'categoria', 
                }
            ),
            'imagen' : forms.FileInput(
                attrs={
                    'class': 'form-control',
                    'id' : 'imagen',
                }
            ),
    } #CIERRE DE WIDGETS

# LOGIN FORM


class LoginForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        "class":"form-control"
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        "class":"form-control"
    }))




# class ContactoForm(forms.ModelForm):

#     class Meta:
#         model = Contacto
#         fields = ["nombre", "correo", "asunto", "mensaje"]
#         labels = {          
#             'nombre': 'Nombre',
#             'correo': 'Correo', 
#             'asunto': 'Asunto', 
#             'mensaje': 'Mensaje', 
#         }
#         widgets = {
#             'nombre' : forms.TextInput(
#                 attrs={
#                     'class' : 'form-control',
#                     'placeholder' : 'Ingrese nombre..',
#                     'id':'nombre', 
#                 }
#             ),
    
#     } #CIERRE DE WIDGETS




# class RegistroUserForm(forms.ModelForm):
#     REGION_CHOICES = [
#         ('region_metropolitana', 'Región Metropolitana'),
#         # Agrega más opciones de regiones aquí
#     ]
#     COMUNA_CHOICES = [
#         ('vitacura','Vitacura'),
#         ('santiago','Santiago'),
#         ('san_ramon','San Ramón'),
#         ('san_miguel','San Miguel'),
#         ('san_ramon','San Joaquín'),
#         ('renca','Renca'),
#         ('recoleta','Recoleta'),
#         ('quinta_normal','Quinta Normal'),
#         ('quilicura','Quilicura'),
#         ('pudahuel','Pudahuel'),
#         ('providencia','Providencia'),
#         ('peñalolen','Peñalolén'),
#         ('pedro_aguirre_cerda','Pedro Aguirre Cerda'),
#         ('ñuñoa','Ñuñoa'),
#         ('maipu','Maipú'),
#         ('macul','Macul'),
#         ('lo_prado','Lo Prado'),
#         ('lo_espejo','Lo Espejo'),
#         ('lo_barnechea','Lo Barnechea'),
#         ('las_condes','Las Condes'),
#         ('la_reina','La Reina'),
#         ('la_pintana','La Pintana'),
#         ('la_granja','La Granja'),
#         ('la_florida','La Florida'),
#         ('la_cisterna','La Cisterna'),
#         ('independencia','Independencia'),
#         ('huechuraba','Huechuraba'),
#         ('estacion_central','Estación Central'),
#         ('el_bosque','El Bosque'),
#         ('conchali','Conchalí'),
#         ('cerro_navia','Cerro Navia'),
#         ('cerrillos','Cerrillos'),   
#         # Agrega más opciones de comunas aquí
#     ]
    
#     class Meta:
#         model = User
#         fields = ['nombre','correo_electronico', 'apellido_P', 'apellido_M', 'fecha_nacimiento', 'region', 'rut', 'telefono', 'comuna', 'calle', 'numeracion', 'imagen_usu']
#         labels = {
#             'nombre': 'Nombre',
#             'correo_electronico': 'Correo Electronico',
#             'apellido_P' : 'Apellido Paterno',
#             'apellido_M' : 'Apellido Materno',
#             'fecha_nacimiento' : 'Fecha de nacimiento',
#             'region' : 'Región',
#             'rut' : 'Rut',
#             'telefono' : 'Telefono',
#             'comuna' : 'Comuna',
#             'calle' : 'Calle',
#             'numeracion' : 'Numeracion',
#             'imagen_usu' : 'Imagen',
#         }
#         widgets = {
#             'nombre' : forms.TextInput(
#                 attrs={
#                     'class' : 'form-control',
#                     'placeholder' : 'Ingrese nombre..',
#                     'id':'nombre', 
#                 }
#             ),
#             'correo_electronico' : forms.EmailInput(
#                 attrs={
#                     'class': 'form-control',
#                     'placeholder': 'Ingrese su correo..',
#                     'id': 'correo',
#                 }
#             ),
#             'calle' : forms.TextInput(
#                 attrs={
#                     'class' : 'form-control',
#                     'placeholder' : 'Ingrese dirección..',
#                     'id':'dirección', 
#                 }
#             ),
#             'imagen_usu' : forms.FileInput(
#                 attrs={
#                     'class': 'form-control',
#                     'id' : 'imagen',
#                 }
#             ),
#     } #CIERRE DE WIDGETS