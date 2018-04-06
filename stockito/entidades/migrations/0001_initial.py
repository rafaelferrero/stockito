# Generated by Django 2.0.4 on 2018-04-06 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('telefono', models.CharField(blank=True, help_text='Ej.: +549 (3564) 55-4433', max_length=20, verbose_name='Teléfono')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='E-Mail')),
                ('nombre', models.CharField(max_length=255, verbose_name='Nombre')),
                ('apellido', models.CharField(max_length=255, verbose_name='Apellido')),
            ],
            options={
                'verbose_name_plural': 'Clientes',
                'ordering': ['apellido', 'nombre'],
                'verbose_name': 'Cliente',
            },
        ),
        migrations.CreateModel(
            name='Proveedor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('telefono', models.CharField(blank=True, help_text='Ej.: +549 (3564) 55-4433', max_length=20, verbose_name='Teléfono')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='E-Mail')),
                ('cuit', models.CharField(blank=True, help_text='Ej.: 30-12345678-5', max_length=13, verbose_name='CUIT')),
                ('razon_social', models.CharField(max_length=255, verbose_name='Razón Social')),
                ('nombre_fantasia', models.CharField(blank=True, max_length=255, verbose_name='Nombre de Fantasía')),
            ],
            options={
                'verbose_name_plural': 'Proveedores',
                'ordering': ['razon_social'],
                'verbose_name': 'Proveedor',
            },
        ),
    ]
