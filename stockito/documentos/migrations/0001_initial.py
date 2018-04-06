# Generated by Django 2.0.4 on 2018-04-06 17:36

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('entidades', '__first__'),
        ('almacenes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DocumentoEgreso',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField(default=django.utils.timezone.now, help_text='Fecha de la transacción', verbose_name='Fecha')),
                ('descripcion', models.CharField(blank=True, help_text='(Opcional) ingrese detalles adicionales', max_length=600, verbose_name='Descripción')),
                ('motivo', models.CharField(help_text='Motivo de la extracción', max_length=500, verbose_name='Motivo')),
                ('cliente', models.ForeignKey(help_text='Persona que solicita el artículo', on_delete=django.db.models.deletion.PROTECT, related_name='clientes_documentoegreso', related_query_name='cliente_documentoegreso', to='entidades.Cliente', verbose_name='Cliente')),
            ],
            options={
                'ordering': ['-fecha', 'cliente'],
                'verbose_name_plural': 'Documentos de Egreso',
                'verbose_name': 'Documento Egreso',
            },
        ),
        migrations.CreateModel(
            name='DocumentoIngreso',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField(default=django.utils.timezone.now, help_text='Fecha de la transacción', verbose_name='Fecha')),
                ('descripcion', models.CharField(blank=True, help_text='(Opcional) ingrese detalles adicionales', max_length=600, verbose_name='Descripción')),
                ('letra', models.CharField(blank=True, choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('E', 'E')], default='A', max_length=1, null=True)),
                ('punto_venta', models.CharField(blank=True, help_text='Punto de venta de la factura de Compra', max_length=4, null=True, verbose_name='Punto de Venta')),
                ('numero', models.CharField(blank=True, help_text='Número de la factura de Compra', max_length=8, null=True, verbose_name='Número')),
                ('importe', models.DecimalField(blank=True, decimal_places=2, help_text='Importe final de la factura', max_digits=8, null=True, verbose_name='Importe')),
                ('proveedor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='proveedores_documentoingreso', related_query_name='proveedor_documentoingreso', to='entidades.Proveedor', verbose_name='Proveedor')),
            ],
            options={
                'ordering': ['-fecha', 'proveedor'],
                'verbose_name_plural': 'Documentos de Ingreso',
                'verbose_name': 'Documento Ingreso',
            },
        ),
        migrations.CreateModel(
            name='Egreso',
            fields=[
                ('movimiento_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='almacenes.Movimiento')),
                ('documento', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='documentos_egreso', related_query_name='documento_egreso', to='documentos.DocumentoEgreso', verbose_name='Documento de Egreso')),
            ],
            options={
                'verbose_name_plural': 'Egresos',
                'verbose_name': 'Egreso',
            },
            bases=('almacenes.movimiento',),
        ),
        migrations.CreateModel(
            name='Ingreso',
            fields=[
                ('movimiento_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='almacenes.Movimiento')),
                ('documento', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='documentos_ingreso', related_query_name='documento_ingreso', to='documentos.DocumentoIngreso', verbose_name='Documento de Ingreso')),
            ],
            options={
                'verbose_name_plural': 'Ingresos',
                'verbose_name': 'Ingreso',
            },
            bases=('almacenes.movimiento',),
        ),
    ]
