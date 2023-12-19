from apps.core.utils.admin import BaseAdminMixin
from django.contrib.admin import ModelAdmin, TabularInline, register
from import_export.admin import ImportExportMixin

from .models import (
    Banner,
    Category,
    Department,
    DescriptionCategory,
    Faculty,
    MainCategory,
    PeriodicityCategory,
    Position,
    PrizePlace,
    Rate,
    Rating,
)


class DepartmentInline(TabularInline):
    """ Инлайновая регистрация кафедры """

    model = Department
    extra = 0


@register(Faculty)
class FacultyAdmin(ImportExportMixin, BaseAdminMixin, ModelAdmin):
    """ Админка Факультета """

    list_display = (
        "short_name",
        "name",
    )

    inlines = [
        DepartmentInline,
    ]


@register(PeriodicityCategory)
class PeriodicityCategoryAdmin(ImportExportMixin, BaseAdminMixin, ModelAdmin):
    """ Админка переодичности измерений """

    list_display = ("text",)


@register(Rate)
class RateAdmin(ImportExportMixin, BaseAdminMixin, ModelAdmin):
    """ Админка ставок """

    list_display = (
        "value",
        "rsue_id",
    )


@register(Banner)
class BannerAdmin(ImportExportMixin, BaseAdminMixin, ModelAdmin):
    """ Админка баннеров """

    list_display = ("text",)


@register(Position)
class PositionAdmin(ImportExportMixin, BaseAdminMixin, ModelAdmin):
    """ Админка Должностей """

    list_display = (
        "pk",
        "name",
        "rsue_id",
    )


@register(Category)
class CategoryAdmin(ImportExportMixin, BaseAdminMixin, ModelAdmin):
    """ Админка Категорий """

    list_display = ("name",)
    search_fields = ["name"]


@register(MainCategory)
class MainCategoryAdmin(ImportExportMixin, BaseAdminMixin, ModelAdmin):
    """ Админка Главных Категорий """

    list_display = ("name",)


class PrizePlaceInline(TabularInline):
    """ Инлайновая призового места """

    model = PrizePlace
    extra = 0


@register(Rating)
class RatingAdmin(ImportExportMixin, BaseAdminMixin, ModelAdmin):
    """ Админка Рейтинга """

    list_display = ("text",)

    inlines = [
        PrizePlaceInline,
    ]


@register(DescriptionCategory)
class DescriptionCategoryAdmin(BaseAdminMixin, ModelAdmin):
    """ Админка Рейтинга """

    search_fields = ["text"]
    list_display = ("text",)
