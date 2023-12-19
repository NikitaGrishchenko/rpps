from django.db import models
from django.utils.translation import gettext_lazy as _


class PeriodicityCategory(models.Model):
    """
    Периодичность измерения
    """

    text = models.CharField(verbose_name=_("Период"), max_length=255)

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = _("Периодичность измерения")
        verbose_name_plural = _("Периодичности измерений")
