from django.db import models
from django.utils.translation import gettext_lazy as _


class Position(models.Model):
    """
    Должность
    """

    short_name = models.CharField(
        max_length=31,
        verbose_name=_("Краткое наименование"),
        blank=True,
        null=True,
    )
    name = models.CharField(_("Наименование"), max_length=255)
    rsue_id = models.IntegerField(_("Публичный id"), blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Должность")
        verbose_name_plural = _("Должности")
