from django.contrib import admin
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
    inlines = [
        IngresoInLIne,
    ]


class EgresoInLIne(admin.TabularInline):
    model = Egreso


@admin.register(DocumentoEgreso)
class DocumentoEgresoAdmin(admin.ModelAdmin):
    inlines = [
        EgresoInLIne,
    ]
