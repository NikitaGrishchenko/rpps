from django.db import models
from django.utils.translation import gettext_lazy as _

from .main_category_questionnaire import MainCategoryQuestionnaire
from .questionnaire_user import QuestionnaireUser


class MainCategoryQuestionnaireUser(models.Model):
    """
    Главная категория анкеты пользователя
    """

    result_point = models.FloatField(
        verbose_name=_("Результирующий балл"), blank=True, null=True, default=0
    )
    result_point_fixed = models.FloatField(
        verbose_name=_("Исправленный балл"), blank=True, null=True
    )
    main_category_questionnaire = models.ForeignKey(
        MainCategoryQuestionnaire,
        blank=True,
        null=True,
        verbose_name=_("Главная категория анкеты"),
        on_delete=models.SET_NULL,
        related_name="main_category_questionnaire_user",
    )
    questionnaire_user = models.ForeignKey(
        QuestionnaireUser,
        blank=True,
        null=True,
        verbose_name=_("Анкета пользователя"),
        on_delete=models.CASCADE,
        related_name="main_category_questionnaire_user",
    )

    def get_actual_points(self):
        """
        Возвращает актуальный балл
        (фактический либо исправленный)
        """
        # TODO: Работает не так ка задуманно
        # (возвращает неверные значения)
        if self.result_point_fixed is None:
            return self.result_point
        return self.result_point_fixed

    def __str__(self):
        return "{0} {1}".format(self.result_point, self.result_point_fixed)

    class Meta:
        verbose_name = _("Главная категория анкеты пользователя")
        verbose_name_plural = _("Главные категории анкеты пользователя")
        unique_together = ["main_category_questionnaire", "questionnaire_user"]
