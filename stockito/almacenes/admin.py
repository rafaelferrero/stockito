from django.contrib import admin
from almacenes.models import Articulo, Deposito, Ubicacion


@admin.register(Articulo)
class ArticuloAdmin(admin.ModelAdmin):
    pass


@admin.register(Deposito)
class DepositoAdmin(admin.ModelAdmin):
    pass


@admin.register(Ubicacion)
class UbicacionAdmin(admin.ModelAdmin):
    pass
