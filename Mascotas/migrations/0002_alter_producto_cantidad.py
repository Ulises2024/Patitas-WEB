# Generated by Django 4.1.5 on 2023-06-03 02:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Mascotas', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='cantidad',
            field=models.IntegerField(default='0', verbose_name='Cantidad'),
        ),
    ]
