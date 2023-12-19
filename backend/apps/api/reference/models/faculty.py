from django.db import models
from django.utils.translation import gettext_lazy as _


class Faculty(models.Model):
    """Факультет"""

    short_name = models.CharField(
        max_length=31, verbose_name=_("Краткое наименование")
    )
    name = models.CharField(max_length=255, verbose_name=_("Наименование"))
    rsue_id = models.IntegerField(_("Публичный id"), blank=True, null=True)
    logo = models.ImageField(_("Логотип"), blank=True, null=True)

    def __str__(self):
        return self.short_name

    class Meta:
        verbose_name = _("Факультет")
        verbose_name_plural = _("Факультеты")
