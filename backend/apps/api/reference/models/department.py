from django.db import models
from django.utils.translation import gettext_lazy as _

from .faculty import Faculty


class Department(models.Model):
    """
    Кафедра
    """

    faculty = models.ForeignKey(
        Faculty,
        models.SET_NULL,
        blank=True,
        null=True,
        verbose_name=_("Факультет"),
        related_name="departments",
    )
    short_name = models.CharField(
        unique=True,
        max_length=31,
        verbose_name=_("Краткое наименование"),
        blank=True,
        null=True,
    )
    name = models.CharField(
        unique=True, max_length=255, verbose_name=_("Наименование")
    )
    rsue_id = models.IntegerField(_("Публичный id"), blank=True, null=True)

    def __str__(self):
        return "{0}, {1}".format(self.faculty.short_name, self.name)

    class Meta:
        verbose_name = _("Кафедра")
        verbose_name_plural = _("Кафедры")
