# Generated by Django 4.1.5 on 2023-06-03 02:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('idCategoria', models.IntegerField(primary_key=True, serialize=False, verbose_name='Id de Categoria')),
                ('nombreCategoria', models.CharField(blank=True, max_length=50, verbose_name='Nombre de Categoria')),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('idNumber', models.CharField(max_length=8, primary_key=True, serialize=False, verbose_name='Id')),
                ('nombre', models.CharField(max_length=45, verbose_name='Nombre')),
                ('descripcion', models.CharField(max_length=300, verbose_name='Descripcion')),
                ('precio', models.IntegerField(verbose_name='Precio')),
                ('cantidad', models.IntegerField(default='Sin stock', verbose_name='Cantidad')),
                ('direccion', models.CharField(default='Av. Esq. Blanca 501, 9251863 Maipú, Región Metropolitana', max_length=100, verbose_name='Direccion')),
                ('Categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Mascotas.categoria', verbose_name='Categoria')),
            ],
        ),
    ]
