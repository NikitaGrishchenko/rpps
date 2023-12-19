from apps.api.reference.models import Department, Position, Rate
from django.db import models
from django.utils.translation import gettext_lazy as _

from .user import User


class UserPosition(models.Model):
    """
    Должность пользователя на кафедре со ставкой
    """

    user = models.ForeignKey(
        User,
        blank=True,
        null=True,
        verbose_name=_("Пользователь"),
        on_delete=models.CASCADE,
        related_name="user_positions",
    )
    department = models.ForeignKey(
        Department,
        verbose_name=_("Кафедра"),
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name="user_positions",
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
        related_name="position",
    )

    def __str__(self):
        return f"{self.user.username} ({self.position}) {self.department}, {self.rate}"

    class Meta:
        verbose_name = _("Должность пользователя")
        verbose_name_plural = _("Должности пользователей")
