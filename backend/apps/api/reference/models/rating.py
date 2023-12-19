from django.db import models
from django.utils.translation import gettext_lazy as _


class Rating(models.Model):
    """
    Рейтинг
    """

    text = models.CharField(verbose_name=_("Наименование"), max_length=255)

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = _("Рейтинг")
        verbose_name_plural = _("Рейтинги")
