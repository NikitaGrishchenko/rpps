from apps.api.auth.models import UserPosition
from django.db import models
from django.utils.translation import gettext_lazy as _

from .questionnaire import Questionnaire


class QuestionnaireUser(models.Model):
    """
    Анкета пользователя
    """

    user_position = models.ForeignKey(
        UserPosition,
        blank=True,
        null=True,
        verbose_name=_("Пользователь"),
        on_delete=models.CASCADE,
        related_name="questionnaire_user",
    )
    questionnaire = models.ForeignKey(
        Questionnaire,
        blank=True,
        null=True,
        verbose_name=_("Анкета"),
        on_delete=models.SET_NULL,
        related_name="questionnaire",
    )
    effective_contract = models.BooleanField(
        verbose_name=_("Эффективный контракт"), blank=True, null=True
    )

    def __str__(self):
        return "{0} {1}".format(self.user_position, self.questionnaire)

    class Meta:
        verbose_name = _("Анкета пользователя")
        verbose_name_plural = _("Анкеты пользователей")
        unique_together = ["user_position", "questionnaire"]
