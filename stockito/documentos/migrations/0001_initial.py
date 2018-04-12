# Generated by Django 2.0.4 on 2018-04-12 13:35

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('almacenes', '0001_initial'),
        ('entidades', '__first__'),
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
                'verbose_name': 'Documento Egreso',
                'verbose_name_plural': 'Documentos de Egreso',
                'ordering': ['-fecha', 'cliente'],
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
                'verbose_name': 'Documento Ingreso',
                'verbose_name_plural': 'Documentos de Ingreso',
                'ordering': ['-fecha', 'proveedor'],
            },
        ),
        migrations.CreateModel(
            name='Movimiento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.PositiveSmallIntegerField(verbose_name='Cantidad')),
                ('multiplicador', models.SmallIntegerField(default=1, help_text='Si el multiplicador es positivo es un ingreso y si es negativo es un egreso')),
            ],
            options={
                'verbose_name': 'Movimiento',
                'verbose_name_plural': 'Movimientos',
                'ordering': ['articulo'],
            },
        ),
        migrations.CreateModel(
            name='Egreso',
            fields=[
                ('movimiento_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='documentos.Movimiento')),
                ('documento', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='documentos_egreso', related_query_name='documento_egreso', to='documentos.DocumentoEgreso', verbose_name='Documento de Egreso')),
            ],
            options={
                'verbose_name': 'Egreso',
                'verbose_name_plural': 'Egresos',
            },
            bases=('documentos.movimiento',),
        ),
        migrations.CreateModel(
            name='Ingreso',
            fields=[
                ('movimiento_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='documentos.Movimiento')),
                ('documento', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='documentos_ingreso', related_query_name='documento_ingreso', to='documentos.DocumentoIngreso', verbose_name='Documento de Ingreso')),
            ],
            options={
                'verbose_name': 'Ingreso',
                'verbose_name_plural': 'Ingresos',
            },
            bases=('documentos.movimiento',),
        ),
        migrations.AddField(
            model_name='movimiento',
            name='articulo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='movimientos_articulo', related_query_name='movimiento_articulo', to='almacenes.Articulo', verbose_name='Artículo'),
        ),
    ]
