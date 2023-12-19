from apps.api.auth.models import UserFile
from apps.api.reference.models import PrizePlace
from django.db import models
from django.utils.translation import gettext_lazy as _

from .category_questionnaire_user import CategoryQuestionnaireUser


class FileCategoryQuestionnaireUser(models.Model):
    """
    Прикрепленный файл
    """

    quantity_value = models.FloatField(
        verbose_name=_("Количественное значение, введенное пользователем"),
        blank=True,
        null=True,
    )
    prize_place = models.ForeignKey(
        PrizePlace,
        verbose_name=_("Призовое место"),
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
    )
    category_questionnaire = models.ForeignKey(
        CategoryQuestionnaireUser,
        verbose_name=_("Категория анкеты пользователя"),
        blank=True,
        null=True,
        on_delete=models.CASCADE,
        related_name="files",
    )
    file = models.ForeignKey(
        UserFile,
        verbose_name=_("файл пользователя"),
        blank=True,
        null=True,
        on_delete=models.PROTECT,
        related_name="file_category_questionnaire_user",
    )
    coefficient = models.FloatField(
        verbose_name=_("Коэффициент соавторства"), blank=True, null=True
    )
    internet_resource_link = models.URLField(
        verbose_name=_("Ссылка на Интернет-ресурс"), blank=True, null=True
    )

    class Meta:
        verbose_name = _("Прикрепленный файл")
        verbose_name_plural = _("Прикрепленные файлы")
