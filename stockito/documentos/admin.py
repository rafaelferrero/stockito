from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from documentos.models import (
    DocumentoIngreso,
    Ingreso,
    DocumentoEgreso,
    Egreso,
)


class IngresoInLIne(admin.TabularInline):
    model = Ingreso


@admin.register(DocumentoIngreso)
class DocumentoIngresoAdmin(admin.ModelAdmin):
    actions_on_bottom = True
    inlines = [
        IngresoInLIne,
    ]
    fieldsets = (
        (None, {
            'fields': (
                (
                    'proveedor',
                    'fecha',
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


@admin.register(DocumentoEgreso)
class DocumentoEgresoAdmin(admin.ModelAdmin):
    inlines = [
        EgresoInLIne,
    ]
