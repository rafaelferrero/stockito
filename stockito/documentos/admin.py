from django.contrib import admin
from django.db.models import F, ExpressionWrapper, IntegerField, CharField
from django.utils.translation import ugettext_lazy as _
from documentos.models import (
    DocumentoIngreso,
    Ingreso,
    DocumentoEgreso,
    Egreso,
    Movimiento,
)


@admin.register(Movimiento)
class MovimientoAdmin(admin.ModelAdmin):
    actions_on_bottom = True
    list_per_page = 25
    fieldsets = (
        (None, {
            'fields': (
                'articulo',
                'cantidad',
                'multiplicador',
                )
        }),
    )
    list_display = (
        'articulo',
        'cantidad_comprometida',
        'comprobante',
        'fecha',
    )
    list_filter = (
        'articulo',
    )
    search_fields = (
        'articulo__codigo',
        'articulo__descripcion',
        'articulo__proveedor__razon_social',
        'articulo__proveedor__nombre_fantasia',
    )

    def get_queryset(self, request):
        qs = super(MovimientoAdmin, self).get_queryset(request)
        qs = qs.annotate(
            Cantidad=ExpressionWrapper(
                F('cantidad')*F('multiplicador'),
                output_field=IntegerField())).order_by('cantidad')
        return qs

    def cantidad_comprometida(self, obj):
        return obj.Cantidad
    cantidad_comprometida.admin_order_field = 'Cantidad'
    cantidad_comprometida.short_description = _('Cantidad')

    def comprobante(self, obj):
        try:
            if hasattr(obj, 'ingreso'):
                return obj.ingreso.documento
            elif hasattr(obj, 'egreso'):
                return obj.egreso.documento
        except NotImplementedError:
            return ""
    comprobante.short_description = _('Comprobante')

    def fecha(self, obj):
        try:
            if hasattr(obj, 'ingreso'):
                return obj.ingreso.documento.fecha
            elif hasattr(obj, 'egreso'):
                return obj.egreso.documento.fecha
        except NotImplementedError:
            return ""
    fecha.short_description = _('Fecha')


class IngresoInLIne(admin.TabularInline):
    model = Ingreso
    exclude = ['multiplicador']


@admin.register(DocumentoIngreso)
class DocumentoIngresoAdmin(admin.ModelAdmin):
    actions_on_bottom = True
    list_per_page = 25
    inlines = [
        IngresoInLIne,
    ]
    fieldsets = (
        (None, {
            'fields': (
                (
                    'fecha',
                    'proveedor',
                ),
                )}),
        ('Campos Opcionales', {
            'classes': ('grp-collapse grp-closed',),
            'fields': (
                (
                    'letra',
                    'punto_venta',
                    'numero',
                ),
                'importe',
                'descripcion',
            ),
        }),
    )
    date_hierarchy = 'fecha'
    list_display = (
        'fecha',
        'proveedor',
        'factura',
    )
    list_filter = (
        'proveedor',
    )
    search_fields = (
        'letra',
        'punto_venta',
        'numero',
        'proveedor__razon_social',
        'proveedor__nombre_fantasia',
        'descripcion',
    )

    def factura(self, obj):
        if obj.letra and obj.punto_venta and obj.numero:
            valor = "Factura {} {}-{}".format(
                obj.letra,
                "0" * (4 - len(obj.punto_venta.strip())) + obj.punto_venta.strip(),
                "0" * (8 - len(obj.numero.strip())) + obj.numero.strip(),
            )
        else:
            valor = ''
        return valor
    factura.short_description = _('Facturas')


class EgresoInLIne(admin.TabularInline):
    model = Egreso
    exclude = ['multiplicador']


@admin.register(DocumentoEgreso)
class DocumentoEgresoAdmin(admin.ModelAdmin):
    actions_on_bottom = True
    list_per_page = 25
    inlines = [
        EgresoInLIne,
    ]
    fieldsets = (
        (None, {
            'fields': (
                (
                    'fecha',
                    'cliente',
                ),
                'motivo',
                )}),
        ('Campos Opcionales', {
            'classes': ('grp-collapse grp-closed',),
            'fields': (
                'descripcion',
            ),
        }),
    )
    date_hierarchy = 'fecha'
    list_display = (
        'fecha',
        'cliente',
    )
    list_filter = (
        'cliente',
    )
    search_fields = (
        'cliente__nombre',
        'cliente__apellido',
        'motivo',
        'descripcion',
    )
