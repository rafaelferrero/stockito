from django.db import models


class Deposito(models.Model):
    deposito = models.ForeignKey(
        'Deposito',
        verbose_name="Depósito Padre",
        blank=True,
    )
    identificacion = models.CharField(
        max_length=255,
        verbose_name="Identificación del Depósito",
        help_text="Ej. Estantería 01",
    )

    def __str__(self):
        deposito=""
        if self.deposito:
            deposito = " (en {})".format(self.deposito)

        return "{}{}".format(self.identificacion,deposito)


