from django.contrib import admin
from almacenes.models import Articulo, Deposito, Ubicacion, Movimiento


@admin.register(Articulo)
class ArticuloAdmin(admin.ModelAdmin):
    pass


@admin.register(Deposito)
class DepositoAdmin(admin.ModelAdmin):
    pass


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


@admin.register(Movimiento)
class MovimientoAdmin(admin.ModelAdmin):
    actions_on_bottom = True
    list_per_page = 25
    fieldsets = (
        (None, {
            'fields': (
                'articulo',
                'cantidad',
                )
        }),
    )
    list_display = (
        'articulo',
        'cantidad',
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
