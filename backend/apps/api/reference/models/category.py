from django.db import models
from django.utils.translation import gettext_lazy as _

from .description_category import DescriptionCategory


class Category(models.Model):
    """
    Категории
    """

    name = models.CharField(_("Наименование"), max_length=500)
    description = models.ForeignKey(
        DescriptionCategory,
        verbose_name=_("Справочник описаний Описание"),
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name="description",
    )

    def __str__(self):
        return f"{self.name} /// {self.description}"

    class Meta:
        ordering = ["name"]
        verbose_name = _("Категория")
        verbose_name_plural = _("Категории")
