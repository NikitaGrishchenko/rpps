from django.db import models
from django.utils.translation import gettext_lazy as _


class DescriptionCategory(models.Model):
    """
    Описание категории
    """

    text = models.TextField(verbose_name=_("Текст описания"), unique=True)

    def __str__(self):
        return self.text

    class Meta:
        ordering = ["text"]
        verbose_name = _("Описание категории")
        verbose_name_plural = _("Описания категорий")
