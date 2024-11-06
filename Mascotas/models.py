from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Categoria(models.Model):
    idCategoria = models.IntegerField(primary_key=True, verbose_name = "Id de Categoria")
    nombreCategoria = models.CharField(max_length = 50, blank = True, verbose_name = "Nombre de Categoria")

    def __str__(self):
        return self.nombreCategoria #Permite acceder a los objetos a traves de su nombre en el ADMIN.


class Producto(models.Model):
    idNumber = models.CharField(primary_key = True, max_length = 8, verbose_name = "Id")
    nombre = models.CharField(max_length = 45, blank= False, null = False, verbose_name= "Nombre")
    marca = models.CharField(max_length=45, blank=False, null=False, default='Sin especificar', verbose_name="Marca")
    precio = models.IntegerField(blank=False, null=False, default='0' , verbose_name = "Precio")
    descripcion = models.CharField(max_length = 300, blank = False, null = False, verbose_name= "Descripcion")
    cantidad = models.IntegerField(blank=False, null=False, default='0', verbose_name = "Cantidad")
    direccion = models.CharField(max_length=100, blank=False, null=False, verbose_name="Direccion", default='Av. Esq. Blanca 501, 9251863 Maipú, Región Metropolitana')
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, verbose_name = "Categoria")
    imagen = models.ImageField(upload_to="imagenes", null=True, blank=True, verbose_name="Imagen")
    favorito = models.BooleanField(null=False, default=False)

    def __str__(self):
        return self.nombre


class Contacto(models.Model):
    nombre = models.CharField(max_length = 45, blank= False, null = False, verbose_name= "Nombre")
    correo = models.EmailField(blank=False, null=False, verbose_name="Correo" )
    asunto = models.CharField(max_length = 100, blank= False, null = False, verbose_name= "Asunto")
    mensaje = models.TextField(max_length = 300, blank=False, null = False, verbose_name= "Mensaje")

    def __str__(self):
        return __str__(self.nombre)


#CLASE DE REGISTRO DE USUARIO
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    telefono = models.CharField(max_length=20)
    imagen_usu = models.ImageField(upload_to='profile_images')

    # Otros campos adicionales

    def __str__(self):
        return self.user.username
    


class RegistroUserForm(models.Model):
    
    REGION_CHOICES = [
        ('region_metropolitana', 'Región Metropolitana'),
        # Agrega más opciones de regiones aquí
    ]
    COMUNA_CHOICES = [
        ('vitacura','Vitacura'),
        ('santiago','Santiago'),
        ('san_ramon','San Ramón'),
        ('san_miguel','San Miguel'),
        ('san_ramon','San Joaquín'),
        ('renca','Renca'),
        ('recoleta','Recoleta'),
        ('quinta_normal','Quinta Normal'),
        ('quilicura','Quilicura'),
        ('pudahuel','Pudahuel'),
        ('providencia','Providencia'),
        ('peñalolen','Peñalolén'),
        ('pedro_aguirre_cerda','Pedro Aguirre Cerda'),
        ('ñuñoa','Ñuñoa'),
        ('maipu','Maipú'),
        ('macul','Macul'),
        ('lo_prado','Lo Prado'),
        ('lo_espejo','Lo Espejo'),
        ('lo_barnechea','Lo Barnechea'),
        ('las_condes','Las Condes'),
        ('la_reina','La Reina'),
        ('la_pintana','La Pintana'),
        ('la_granja','La Granja'),
        ('la_florida','La Florida'),
        ('la_cisterna','La Cisterna'),
        ('independencia','Independencia'),
        ('huechuraba','Huechuraba'),
        ('estacion_central','Estación Central'),
        ('el_bosque','El Bosque'),
        ('conchali','Conchalí'),
        ('cerro_navia','Cerro Navia'),
        ('cerrillos','Cerrillos'),   
        # Agrega más opciones de comunas aquí
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    nombre = models.CharField(max_length = 50, blank= False, null = False, verbose_name= "Nombre")
    correo_electronico = models.EmailField(unique=True, null=False, blank=False, verbose_name='Correo Electrónico')
    apellido_P = models.CharField(max_length=100, blank=False, null=False, verbose_name='Apellido Paterno')
    apellido_M = models.CharField(max_length=100, blank=False, null=False,verbose_name='Apellido Materno')
    fecha_nacimiento = models.DateField(verbose_name='Fecha de Nacimiento')
    region = models.CharField(max_length=100, choices=REGION_CHOICES, verbose_name="Región")
    rut = models.CharField(unique=True, max_length=20, verbose_name='Rut')
    telefono = models.CharField(max_length=20, verbose_name='Teléfono')
    comuna = models.CharField(max_length=100, choices=COMUNA_CHOICES, verbose_name="Comuna")
    calle = models.CharField(max_length=100, null=False, blank=False, verbose_name="Calle")
    numeracion = models.CharField(max_length=20, verbose_name='Numeración')

    # ... otros campos y métodos adicionales ...

    def __str__(self):
        return self.rut