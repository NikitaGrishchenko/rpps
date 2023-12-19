from apps.api.reference.enums import TYPE_CATEGORY
from apps.api.reference.models import Category, PeriodicityCategory, Rating
from django.db import models
from django.utils.translation import gettext_lazy as _

from .main_category_questionnaire import MainCategoryQuestionnaire


class CategoryQuestionnaire(models.Model):
    """
    Категория Анкеты
    """

    number = models.PositiveIntegerField(
        verbose_name=_("Номер категории"),
        blank=True,
        null=True,
    )
    reference_category = models.ForeignKey(
        Category,
        blank=True,
        null=True,
        verbose_name=_("Справочник Категорий"),
        on_delete=models.SET_NULL,
    )
    periodicity = models.ForeignKey(
        PeriodicityCategory,
        verbose_name=_("Периодичность измерения"),
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
    )
    main_category = models.ForeignKey(
        MainCategoryQuestionnaire,
        blank=True,
        null=True,
        verbose_name=_("Главная категория"),
        on_delete=models.SET_NULL,
        related_name="category",
    )
    parent = models.ForeignKey(
        "self",
        blank=True,
        null=True,
        verbose_name=_("Родительская категория"),
        on_delete=models.SET_NULL,
        related_name="childrens",
    )
    type_category = models.IntegerField(
        choices=TYPE_CATEGORY,
        verbose_name=_("Тип категории"),
        blank=True,
        null=True,
    )
    rating = models.ForeignKey(
        Rating,
        verbose_name=_("Рейтинг"),
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
    )
    weight = models.FloatField(
        verbose_name=_("Весомость показателя"), blank=True, null=True
    )
    max_weight = models.FloatField(
        verbose_name=_("Максимальная возможная весомость показателя"),
        blank=True,
        null=True,
    )
    use_internet_resource_link = models.BooleanField(
        verbose_name=_("Добавить поле для Интернет-ресурса"), default=False
    )
    internet_resource_link_or_doc = models.BooleanField(
        verbose_name=_("Или ссылка на Интернет-ресурс или документ"),
        default=False,
    )

    def __str__(self):
        if self.number is None:
            return "{0} (тип:{1})".format(
                self.reference_category.name, self.type_category
            )
        else:
            return "№{0} {1} (тип:{2})".format(
                self.number, self.reference_category.name, self.type_category
            )

    class Meta:
        ordering = [
            "number",
        ]
        verbose_name = _("Категория Анкеты")
        verbose_name_plural = _("Категории Анкеты")
