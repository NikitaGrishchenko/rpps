from apps.api.reference.models import MainCategory
from django.db import models
from django.utils.translation import gettext_lazy as _

from .questionnaire import Questionnaire


class MainCategoryQuestionnaire(models.Model):
    """
    Главная Категория Анкеты
    """

    number = models.PositiveIntegerField(
        verbose_name=_("Номер категории"), default=0
    )

    reference_category = models.ForeignKey(
        MainCategory,
        blank=True,
        null=True,
        verbose_name=_("Справочник Категорий"),
        on_delete=models.SET_NULL,
        related_name="reference_main_category",
    )
    questionnaire = models.ForeignKey(
        Questionnaire,
        blank=True,
        null=True,
        verbose_name=_("Анкета"),
        on_delete=models.SET_NULL,
        related_name="main_category",
    )

    def __str__(self):
        return f"№{self.number} {self.reference_category.name} ({self.questionnaire.name})"

    class Meta:
        ordering = ["number"]
        verbose_name = _("Главная Категория Анкеты")
        verbose_name_plural = _("Главные Категории Анкеты")
