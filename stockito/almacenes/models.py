from django.db import models
from django.utils.translation import ugettext_lazy as _
from entidades.models import Proveedor
from django.db.models import Sum, F, ExpressionWrapper, IntegerField


class Deposito(models.Model):
    deposito = models.ForeignKey(
        'Deposito',
        related_name="depositos_hijos",
        related_query_name="deposito_hijo",
        verbose_name=_("Depósito Padre"),
        blank=True,
        null=True,
        on_delete=models.PROTECT,
    )
    identificacion = models.CharField(
        max_length=255,
        verbose_name=_("Identificación del Depósito"),
        help_text=_("Ej. Estantería 01"),
    )

    class Meta:
        verbose_name = _("Deposito")
        verbose_name_plural = _("Depósitos")
        ordering = ['identificacion']

    def __str__(self):
        deposito = ""
        if self.deposito:
            deposito = " (en {})".format(self.deposito)

        return "{}{}".format(self.identificacion, deposito)


class Articulo(models.Model):
    codigo = models.CharField(
        max_length=255,
        verbose_name=_("Identificador"),
        help_text=_("Código de Identificación Interna"),
    )
    descripcion = models.CharField(
        max_length=255,
        verbose_name=_("Descripción"),
        help_text=_("Descripción del Artículo"),
    )
    proveedor = models.ForeignKey(
        Proveedor,
        related_name="proveedores_articulo",
        related_query_name="proveedor_articulo",
        verbose_name=_("Proveedor"),
        help_text=_(
            "Si el mismo artículo lo proveen empresas distintas"
            " es preferible cargar dos artículos distintos"
        ),
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
    )

    class Meta:
        verbose_name = _("Artículo")
        verbose_name_plural = _("Artículos")
        ordering = ['codigo', 'proveedor']

    @property
    def disponibilidad(self):
        return self.movimientos_articulo.all().annotate(
            cant=ExpressionWrapper(
                F('cantidad')*F('multiplicador'), output_field=IntegerField())
        ).aggregate(Sum('cant'))['cant__sum']

    def __str__(self):
        return "{} - {}".format(
            self.codigo,
            self.descripcion,
        )


class Ubicacion(models.Model):
    ubicacion = models.ForeignKey(
        Deposito,
        verbose_name=_("Ubicación."),
        help_text=_("Ubicación donde se almacena el artículo en el Depósito"),
        related_name="ubicaciones_deposito",
        related_query_name="ubicacion_deposito",
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
    )
    articulo = models.ForeignKey(
        Articulo,
        verbose_name=_("Artículo"),
        related_name="articulos_ubicacion",
        related_query_name="articulo_ubicacion",
        on_delete=models.PROTECT,
    )

    class Meta:
        verbose_name = _("Ubicación")
        verbose_name_plural = _("Ubicaciones")
        ordering = ['ubicacion', 'articulo']

    def __str__(self):
        return "{}".format(self.ubicacion.identificacion)
