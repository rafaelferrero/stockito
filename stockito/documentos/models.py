from django.db import models
from django.utils import timezone
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
from entidades.models import Proveedor, Cliente
from almacenes.models import Articulo
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
        verbose_name = _("Documento")
        verbose_name_plural = _("Documentos")


class DocumentoIngreso(Documento):
    proveedor = models.ForeignKey(
        Proveedor,
        related_name="proveedores_documentoingreso",
        related_query_name="proveedor_documentoingreso",
        verbose_name=_("Proveedor"),
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
    )
    letra = models.CharField(
        max_length=1,
        choices=LETRA,
        default=LETRA[0][0],
        blank=True,
        null=True,
    )
    punto_venta = models.CharField(
        max_length=4,
        verbose_name=_("Punto de Venta"),
        help_text=_("Punto de venta de la factura de Compra"),
        blank=True,
        null=True,
    )
    numero = models.CharField(
        max_length=8,
        verbose_name=_("Número"),
        help_text=_("Número de la factura de Compra"),
        blank=True,
        null=True,
    )
    importe = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        verbose_name=_("Importe"),
        help_text=_("Importe final de la factura"),
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name = _("Documento Ingreso")
        verbose_name_plural = _("Documentos de Ingreso")
        ordering = ['-fecha', 'proveedor']

    def __str__(self):
        if not self.punto_venta:
            self.punto_venta = ''
        if not self.numero:
            self.numero = ''

        valor = ''
        if self.letra and self.punto_venta and self.numero:
            valor = "Factura {} {}-{} del ".format(
                self.letra,
                "0" * (4 - len(self.punto_venta.strip())) + self.punto_venta.strip(),
                "0" * (8 - len(self.numero.strip())) + self.numero.strip(),
            )

        return valor + "{} ({})".format(
            self.fecha,
            self.proveedor,
        )

    def clean(self):
        if self.punto_venta and not self.numero:
            raise ValidationError(
                {'numero':
                 _("Si decide indicar una factura de compra,"
                   " no omita el número de la misma")})
        if not self.punto_venta and self.numero:
            raise ValidationError(
                {'punto_venta':
                 _("Si decide indicar una factura de compra,"
                   " no omita el punto de venta de la misma")})
        if self.punto_venta and self.numero and not self.letra:
            raise ValidationError(
                {'letra':
                 _("Si decide indicar una factura de compra,"
                   " no omita la letra de la misma")})

    def save(self, *args, **kwargs):
        if not self.punto_venta and not self.numero:
            self.letra = ''
        super(DocumentoIngreso, self).save(*args, **kwargs)


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

    class Meta:
        verbose_name = _("Documento Egreso")
        verbose_name_plural = _("Documentos de Egreso")
        ordering = ['-fecha', 'cliente']

    def __str__(self):
        return "{} {}".format(
            self.cliente,
            self.fecha,
        )


class Movimiento(models.Model):
    articulo = models.ForeignKey(
        Articulo,
        verbose_name=_("Artículo"),
        related_name="movimientos_articulo",
        related_query_name="movimiento_articulo",
        on_delete=models.PROTECT,
    )
    cantidad = models.SmallIntegerField(
        verbose_name=_("Cantidad"),
    )

    class Meta:
        verbose_name = _("Movimiento")
        verbose_name_plural = _("Movimientos")
        ordering = ['articulo']

    def __str__(self):
        return "{} cantidad: {}".format(
            self.articulo,
            self.cantidad,
        )


class Ingreso(Movimiento):
    documento = models.ForeignKey(
        DocumentoIngreso,
        verbose_name=_("Documento de Ingreso"),
        related_name="documentos_ingreso",
        related_query_name="documento_ingreso",
        on_delete=models.PROTECT,
    )

    class Meta:
        verbose_name = _("Ingreso")
        verbose_name_plural = _("Ingresos")


class Egreso(Movimiento):
    documento = models.ForeignKey(
        DocumentoEgreso,
        verbose_name=_("Documento de Egreso"),
        related_name="documentos_egreso",
        related_query_name="documento_egreso",
        on_delete=models.PROTECT,
    )

    class Meta:
        verbose_name = _("Egreso")
        verbose_name_plural = _("Egresos")

    def save(self, *args, **kwargs):
        if not self.pk:
            self.cantidad = self.cantidad * (-1)
        super(Movimiento, self).save(*args, **kwargs)
