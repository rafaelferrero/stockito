from django.db import models
from django.utils.translation import ugettext_lazy as _


class Entidad(models.Model):
    telefono = models.CharField(
        max_length=20,
        verbose_name=_("Teléfono"),
        help_text=_("Ej.: +549 (3564) 55-4433"),
        blank=True,
    )
    email = models.EmailField(
        verbose_name=_("E-Mail"),
        blank=True,
    )

    class Meta:
        abstract = True


class Cliente(Entidad):
    nombre = models.CharField(
        max_length=255,
        verbose_name=_("Nombre"),
    )
    apellido = models.CharField(
        max_length=255,
        verbose_name=_("Apellido"),
    )

    def __str__(self):
        return "{}, {}".format(
            self.apellido.upper(),
            self.nombre.title(),
        )


class Proveedor(Entidad):
    cuit = models.CharField(
        max_length=13,
        verbose_name=_("CUIT"),
        help_text=_("Ej.: 30-12345678-5"),
        blank=True,
    )
    razon_social = models.CharField(
        max_length=255,
        verbose_name=_("Razón Social"),
    )
    nombre_fantasia = models.CharField(
        max_length=255,
        verbose_name=_("Nombre de Fantasía"),
        blank=True,
    )

    @property
    def nombre_completo(self):
        r = self.razon_social.title()
        if self.cuit:
            c = "( {} )".format(self.cuit)
        if self.nombre_fantasia:
            n = "{}".format(self.nombre_fantasia.title())

        if c and n:
            identificacion = "'{}' - {} {}".format(n, r, c)
        elif not c and n:
            identificacion = "'{}' - {}".format(n, r)
        elif c and not n:
            identificacion = "{} {}".format(r, c,)
        else:
            identificacion = "{}".format(r)

        return identificacion

    def __str__(self):
        return "{}".format(self.razon_social.title())
