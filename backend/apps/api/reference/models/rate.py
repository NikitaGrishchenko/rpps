from django.db import models
from django.utils.translation import gettext_lazy as _


class Rate(models.Model):
    """
    Ставка
    """

    value = models.FloatField(unique=True, verbose_name=_("Значение"))
    rsue_id = models.IntegerField(_("Публичный id"), blank=True, null=True)

    def __str__(self):
        return str(self.value)

    class Meta:
        verbose_name = _("Ставка")
        verbose_name_plural = _("Ставки")
