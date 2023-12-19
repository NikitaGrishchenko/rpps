from django.db import models
from django.utils.translation import gettext_lazy as _

from .category_questionnaire import CategoryQuestionnaire
from .questionnaire_user import QuestionnaireUser


class CategoryQuestionnaireUser(models.Model):
    """
    Категория Анкеты Пользователя
    """

    questionnaire_user = models.ForeignKey(
        QuestionnaireUser,
        blank=True,
        null=True,
        verbose_name=_("Анкета пользователя"),
        on_delete=models.SET_NULL,
    )
    category_questionnaire = models.ForeignKey(
        CategoryQuestionnaire,
        blank=True,
        null=True,
        verbose_name=_("Категория анкеты"),
        on_delete=models.SET_NULL,
        related_name="category_questionnaire_user",
    )
    result_point = models.FloatField(
        verbose_name=_("Результирующий балл"), default=0
    )
    result_point_fixed = models.FloatField(
        verbose_name=_("Исправленный балл"), blank=True, null=True
    )
    is_verified = models.BooleanField(
        blank=True, null=True, verbose_name=_("Категория проверена?")
    )

    def get_actual_points(self):
        """
        Возвращает актуальный балл
        (фактический либо исправленный)
        """
        if self.result_point_fixed:
            return self.result_point_fixed
        return self.result_point

    def __str__(self):
        return "{0} {1}".format(
            self.category_questionnaire, self.questionnaire_user
        )

    class Meta:
        verbose_name = _("Категория Анкеты  Пользователя")
        verbose_name_plural = _("Категории Анкеты Пользователей")
        unique_together = ["questionnaire_user", "category_questionnaire"]
