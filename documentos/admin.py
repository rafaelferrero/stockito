from django.contrib import admin
from documentos.models import (
    DocumentoIngreso,
    Ingreso
)


class IngresoInLIne(admin.TabularInline):
    model = Ingreso


@admin.register(DocumentoIngreso)
class DocumentoIngresoAdmin(admin.ModelAdmin):
    inlines = [
        IngresoInLIne,
    ]
