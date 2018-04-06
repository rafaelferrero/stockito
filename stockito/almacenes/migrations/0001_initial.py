# Generated by Django 2.0.4 on 2018-04-06 17:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('entidades', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Articulo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(help_text='Código de Identificación Interna', max_length=255, verbose_name='Identificador')),
                ('descripcion', models.CharField(help_text='Descripción del Artículo', max_length=255, verbose_name='Descripción')),
                ('proveedor', models.ForeignKey(blank=True, help_text='Si el mismo artículo lo proveen empresas distintas es preferible cargar dos artículos distintos', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='proveedores_articulo', related_query_name='proveedor_articulo', to='entidades.Proveedor', verbose_name='Proveedor')),
            ],
            options={
                'ordering': ['codigo', 'proveedor'],
                'verbose_name_plural': 'Artículos',
                'verbose_name': 'Artículo',
            },
        ),
        migrations.CreateModel(
            name='Deposito',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('identificacion', models.CharField(help_text='Ej. Estantería 01', max_length=255, verbose_name='Identificación del Depósito')),
                ('deposito', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='depositos_hijos', related_query_name='deposito_hijo', to='almacenes.Deposito', verbose_name='Depósito Padre')),
            ],
            options={
                'ordering': ['deposito', 'identificacion'],
                'verbose_name_plural': 'Depósitos',
                'verbose_name': 'Deposito',
            },
        ),
        migrations.CreateModel(
            name='Movimiento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.SmallIntegerField(verbose_name='Cantidad')),
                ('articulo', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='movimientos_articulo', related_query_name='movimiento_articulo', to='almacenes.Articulo', verbose_name='Artículo')),
            ],
            options={
                'ordering': ['articulo'],
                'verbose_name_plural': 'Movimientos',
                'verbose_name': 'Movimiento',
            },
        ),
        migrations.CreateModel(
            name='Ubicacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('articulo', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='articulos_ubicacion', related_query_name='articulo_ubicacion', to='almacenes.Articulo', verbose_name='Artículo')),
                ('ubicacion', models.ForeignKey(blank=True, help_text='Ubicación donde se almacena el artículo en el Depósito', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='ubicaciones_deposito', related_query_name='ubicacion_deposito', to='almacenes.Deposito', verbose_name='Ubicación.')),
            ],
            options={
                'ordering': ['ubicacion', 'articulo'],
                'verbose_name_plural': 'Ubicaciones',
                'verbose_name': 'Ubicación',
            },
        ),
    ]
