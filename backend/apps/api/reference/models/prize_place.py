from django.db import models
from django.utils.translation import gettext_lazy as _

from .rating import Rating


class PrizePlace(models.Model):
    """
    Призовое место
    """

    rating = models.ForeignKey(
        Rating,
        verbose_name=_("Наименование"),
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )
    points = models.FloatField(verbose_name=_("Баллы"), blank=True, null=True)
    name = models.CharField(verbose_name=_("Наименование"), max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Призовое место")
        verbose_name_plural = _("Призовые места")
