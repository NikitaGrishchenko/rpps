from apps.api.reference.enums import STATUS_QUESTIONARY
from django.db import models
from django.utils.translation import gettext_lazy as _


class Questionnaire(models.Model):
    """
    Анкета
    """

    file = models.FileField(
        verbose_name=_("Файл анкеты"),
        upload_to="questionnaire/",
        blank=True,
        null=True,
    )

    name = models.CharField(
        verbose_name=_("Текстовое представление"), default="", max_length=255
    )
    status = models.IntegerField(
        choices=STATUS_QUESTIONARY, verbose_name=_("Статус анкеты")
    )
    preview_image = models.ImageField(
        verbose_name=_("Превью"),
        upload_to="questionnaire/img",
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Анкета")
        verbose_name_plural = _("Анкеты")
