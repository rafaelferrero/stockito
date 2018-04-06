from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from entidades.models import Proveedor, Cliente


@admin.register(Proveedor)
class ProveedorAdmin(admin.ModelAdmin):
    actions_on_bottom = True
    list_per_page = 25
    fieldsets = (
        (None, {
            'fields': (
                'razon_social',
            )
        }),
        ('Campos Opcionales', {
            'classes': ('grp-collapse grp-closed',),
            'fields': (
                'cuit',
                'nombre_fantasia',
                (
                    'telefono',
                    'email',
                ),
            ),
        }),
    )
    list_display = (
        'razon_social',
        'cuit',
        'telefono',
        'email',
    )
    search_fields = (
        'cuit',
        'razon_social',
        'telefono',
        'email',
    )


@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    actions_on_bottom = True
    list_per_page = 25
    fieldsets = (
        (None, {
            'fields': (
                (
                    'apellido',
                    'nombre',
                 ),
            )
        }),
        ('Campos Opcionales', {
            'classes': ('grp-collapse grp-closed',),
            'fields': (
                (
                    'telefono',
                    'email',
                ),
            ),
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
