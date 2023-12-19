from apps.api.reference.models import Department, Position, Rate
from django.db import models
from django.utils.translation import gettext_lazy as _

from .application_submission import ApplicationSubmission


class ApplicationSubmissionPosition(models.Model):
    """
    Должность пользователя на кафедре со ставкой для подачи заявки
    """

    application_submission = models.ForeignKey(
        ApplicationSubmission,
        blank=True,
        null=True,
        verbose_name=_("Пользователь"),
        on_delete=models.CASCADE,
        related_name="application_submission_position"
    )
    department = models.ForeignKey(
        Department,
        verbose_name=_("Кафедра"),
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
    )
    rate = models.ForeignKey(
        Rate,
        verbose_name=_("Ставка"),
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
    )
    position = models.ForeignKey(
        Position,
        verbose_name=_("Должность"),
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
    )

    def __str__(self):
        return f"{self.application_submission.email} ({self.position}) {self.department}, {self.rate}"

    class Meta:
        verbose_name = _("Должность")
        verbose_name_plural = _("Должности")

