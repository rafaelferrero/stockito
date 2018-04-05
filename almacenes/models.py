from django.db import models
from django.utils.translation import ugettext_lazy as _


class Deposito(models.Model):
    deposito = models.ForeignKey(
        'Deposito',
        verbose_name=_("Depósito Padre"),
        blank=True,
    )
    identificacion = models.CharField(
        max_length=255,
        verbose_name=_("Identificación del Depósito"),
        help_text=_("Ej. Estantería 01"),
    )

    def __str__(self):
        deposito=""
        if self.deposito:
            deposito = " (en {})".format(self.deposito)

        return "{}{}".format(self.identificacion, deposito)


