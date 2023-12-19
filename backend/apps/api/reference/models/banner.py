from django.db import models
from django.utils.translation import gettext_lazy as _


class Banner(models.Model):
    """
    Баннер на главной странице анкеты
    """

    text = models.TextField(verbose_name=_("Текст описания"))
    show = models.BooleanField(_("Отображать баннер?"), default=False)
    color_text = models.CharField(
        _("Цвет текста"),
        max_length=50,
        help_text="https://quasar.dev/style/color-palette#introduction",
        null=True,
    )
    color_bg = models.CharField(
        _("Фон баннера"),
        max_length=50,
        help_text="https://quasar.dev/style/color-palette#introduction",
        null=True,
    )
    icon = models.CharField(
        _("Иконка"),
        max_length=50,
        help_text="https://materialdesignicons.com/",
        null=True,
    )
    color_icon = models.CharField(
        _("Цвет иконки"),
        max_length=50,
        help_text="https://quasar.dev/style/color-palette#introduction",
        null=True,
    )

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = _("Баннер")
        verbose_name_plural = _("Баннеры")
