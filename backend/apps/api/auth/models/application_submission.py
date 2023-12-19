from django.db import models
from django.utils.translation import gettext_lazy as _


class ApplicationSubmission(models.Model):
    """
    Подача заявки на регистрацию пользователя
    """

    first_name = models.CharField(_("first name"), max_length=150, blank=True)
    last_name = models.CharField(_("last name"), max_length=150, blank=True)
    patronymic = models.CharField(
        _("Отчество"), max_length=150, blank=True, null=True
    )
    email = models.EmailField(_("email address"), blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        verbose_name = _("Заявка")
        verbose_name_plural = _("Заявки")

