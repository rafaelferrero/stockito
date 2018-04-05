from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _
from entidades.models import Proveedor, Cliente
from almacenes.models import Movimiento
from documentos.choices import LETRA


class Documento(models.Model):
    fecha = models.DateField(
        default=timezone.now,
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
        related_name="proveedores_documentoingreso",
        related_query_name="proveedor_documentoingreso",
        verbose_name=_("Proveedor"),
        on_delete=models.PROTECT,
    )
    letra = models.CharField(
        max_length=1,
        choices=LETRA,
        default=LETRA[0][0],
        help_text=_("Letra de la factura de Compra")
    )
    punto_venta = models.CharField(
        max_length=4,
        help_text=_("Punto de venta de la factura de Compra")
    )
    numero = models.CharField(
        max_length=8,
        help_text=_("Número de la factura de Compra")
    )
    importe = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        verbose_name=_("Importe"),
        help_text=_("Importe final de la factura"),
        blank=True,
    )

    def __str__(self):
        return "Factura {} {}-{} del {} ({})".format(
            self.letra,
            "0" * (4 - len(self.punto_venta.strip())) + self.punto_venta.strip(),
            "0" * (8 - len(self.numero.strip())) + self.numero.strip(),
            self.fecha,
            self.proveedor,
        )


class DocumentoEgreso(Documento):
    cliente = models.ForeignKey(
        Cliente,
        related_name="clientes_documentoegreso",
        related_query_name="cliente_documentoegreso",
        verbose_name=_("Cliente"),
        help_text=_("Persona que solicita el artículo"),
        on_delete=models.PROTECT,
    )
    motivo = models.CharField(
        max_length=500,
        verbose_name=_("Motivo"),
        help_text=_("Motivo de la extracción"),
    )

    def __str__(self):
        return "{} {}".format(
            self.cliente,
            self.fecha,
        )


class Ingreso(Movimiento):
    documento = models.ForeignKey(
        DocumentoIngreso,
        verbose_name=_("Documento de Ingreso"),
        related_name="documentos_ingreso",
        related_query_name="documento_ingreso",
        on_delete=models.PROTECT,
    )


class Egreso(Movimiento):
    documento = models.ForeignKey(
        DocumentoEgreso,
        verbose_name=_("Documento de Egreso"),
        related_name="documentos_egreso",
        related_query_name="documento_egreso",
        on_delete=models.PROTECT,
    )
