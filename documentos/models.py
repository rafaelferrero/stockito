from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _
from entidades.models import Proveedor, Cliente


class Documento(models.Model):
    fecha = models.DateField(
        default=timezone.now(),
        verbose_name=_("Fecha"),
        help_text=_("Fecha de la transacción"),
    )
    descripcion = models.CharField(
        max_length=600,
        verbose_name=_("Descripción"),
        help_text=_("(Opcional) ingrese detalles adicionales"),
        blank=True,
    )

    class Meta:
        abstract = True


class DocumentoIngreso(Documento):
    proveedor = models.ForeignKey(
        Proveedor,
        related_name="proveedor_ingreso",
        verbose_name=_("Proveedor"),
    )
    letra = models.CharField(
        choices=['A', 'B', 'C', 'E'],
    )
    punto_venta = models.CharField(
        max_length=4,
    )
    numero = models.CharField(
        max_length=8,
    )

    def __str__(self):
        return "Factura {} {}-{} {}".format(
            self.letra,
            "0" * (4 - len(self.punto_venta.strip())) + self.punto_venta.strip(),
            "0" * (8 - len(self.numero.strip())) + self.numero.strip(),
            self.proveedor,
        )


class DocumentoEgreso(Documento):
    cliente = models.ForeignKey(
        Cliente,
        related_name="cliente_egreso",
        verbose_name=_("Cliente"),
        help_text=_("Persona que solicita el artículo")
    )
