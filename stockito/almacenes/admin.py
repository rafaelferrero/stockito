from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from almacenes.models import Articulo, Deposito, Ubicacion


@admin.register(Articulo)
class ArticuloAdmin(admin.ModelAdmin):
    actions_on_bottom = True
    list_per_page = 25
    fieldsets = (
        (None, {
            'fields': (
                (
                    'proveedor',
                    'codigo',
                ),
                'descripcion',
            )
        }),
    )
    list_display = (
        'codigo',
        'descripcion',
        'proveedor',
        'disponibilidad',
    )
    list_filter = (
        'proveedor',
    )
    search_fields = (
        'codigo',
        'descripcion',
        'proveedor__razon_social',
        'proveedor__nombre_fantasia',
    )

    def disponibilidad(self, obj):
        return obj.disponibilidad
    disponibilidad.short_description = _('Disponibilidad')


@admin.register(Deposito)
class DepositoAdmin(admin.ModelAdmin):
    actions_on_bottom = True
    list_per_page = 25
    fieldsets = (
        (None, {
            'fields': (
                'identificacion',
                'deposito',
            )
        }),
    )
    list_display = (
        'identificacion',
        'deposito',
    )
    list_filter = (
        'deposito',
    )
    search_fields = (
        'identificacion',
        'deposito__identificacion',
    )


@admin.register(Ubicacion)
class UbicacionAdmin(admin.ModelAdmin):
    actions_on_bottom = True
    list_per_page = 25
    fieldsets = (
        (None, {
            'fields': (
                'ubicacion',
                'articulo',
                )
        }),
    )
    list_display = (
        'ubicacion',
        'articulo',
    )
    list_filter = (
        'ubicacion',
        'articulo',
    )
    search_fields = (
        'ubicacion__identificacion',
        'articulo__codigo',
        'articulo__descripcion',
        'articulo__proveedor__razon_social',
        'articulo__proveedor__nombre_fantasia',
    )
