from django.db import models


class Entidad(models.Model):
    telefono = models.CharField(
        max_length=20,
        verbose_name="Teléfono",
        help_text="Ej.: +549 (3564) 55-4433",
        blank=True,
    )
    email = models.EmailField(
        verbose_name="E-Mail",
    )

    class Meta:
        abstract = True


class Cliente(Entidad):
    nombre = models.CharField(
        max_length=255,
        verbose_name="Nombre",
    )
    apellido = models.CharField(
        max_length=255,
        verbose_name="Apellido",
    )

    def __str__(self):
        return "{}, {}".format(
            self.apellido.upper(),
            self.nombre.tittle(),
        )


class Proveedor(Entidad):
    cuit = models.CharField(
        max_length=13,
        verbose_name="CUIT",
        help_text="Ej.: 30-12345678-5",
        blank=True,
    )
    razon_social = models.CharField(
        max_length=255,
        verbose_name="Razón Social",
    )
    nombre_fantasia = models.CharField(
        max_length=255,
        blank=True,
    )

    @property
    def nombre_completo(self):
        r = self.razon_social.tittle()
        if self.cuit:
            c = "( {} )".format(self.cuit)
        if self.nombre_fantasia:
            n = "{}".format(self.nombre_fantasia.tittle())

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
        return "{}".format(self.razon_social.tittle())
