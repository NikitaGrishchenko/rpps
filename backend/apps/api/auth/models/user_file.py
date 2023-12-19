import datetime

import pytz
from apps.api.reference.enums import TYPE_FILE
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from .user import User

# CURRENT_TZ = pytz.timezone("Europe/Moscow")


class UserFile(models.Model):
    """
    Файл Пользователя
    """

    def user_directory_path(self, filename):
        """
        Возращает директорию сохранения файла
        """
        return "user_{0}/{1}".format(self.user.username, filename)

    user = models.ForeignKey(
        User,
        blank=True,
        null=True,
        verbose_name=_("Пользователь"),
        on_delete=models.CASCADE,
        related_name="files",
    )
    name = models.CharField(verbose_name=_("Наименование"), max_length=255)
    file = models.FileField(
        verbose_name=_("Файл"), upload_to=user_directory_path
    )
    type_file = models.IntegerField(
        choices=TYPE_FILE, verbose_name=_("Тип файла")
    )
    date_upload = models.DateTimeField(default=timezone.now, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Файл пользователя")
        verbose_name_plural = _("Файлы пользователей")
