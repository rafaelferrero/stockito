from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from entidades.models import Proveedor, Cliente


@admin.register(Proveedor)
class ProveedorAdmin(admin.ModelAdmin):
    pass


@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    actions_on_bottom = True
    fieldsets = (
        (None, {
            'fields': (
                (
                    'apellido',
                    'nombre',
                 ),
                (
                    'telefono',
                    'email',
                ),
            )
        }),
    )
    list_display = (
        'nombre_completo',
        'telefono',
        'email',
    )
    list_filter = (
        'apellido',
    )
    search_fields = (
        'apellido',
        'nombre',
        'telefono',
        'email',
    )

    def nombre_completo(self, obj):
        return obj
    nombre_completo.short_description = _('Apellido y Nombre')
