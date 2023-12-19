from django.db import models
from django.utils.translation import gettext_lazy as _


class MainCategory(models.Model):
    """
    Главные категории
    """

    name = models.CharField(_("Наименование"), max_length=255)
    short_name = models.CharField(
        _("Краткое Наименование"), max_length=24, blank=True, null=True
    )

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["name"]
        verbose_name = _("Главная категория")
        verbose_name_plural = _("Главные категории")
