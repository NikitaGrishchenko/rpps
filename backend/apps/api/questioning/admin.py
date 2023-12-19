from apps.core.utils.admin import BaseAdminMixin
from django.contrib.admin import ModelAdmin, TabularInline, register
from django.db.models import Q
from django.db.models.query import Prefetch
from import_export.admin import ImportExportMixin

from .models import (
    CategoryQuestionnaire,
    CategoryQuestionnaireUser,
    FileCategoryQuestionnaireUser,
    MainCategoryQuestionnaire,
    MainCategoryQuestionnaireUser,
    Questionnaire,
    QuestionnaireUser,
)


class MainCategoryQuestionnaireInline(TabularInline):
    """Инлайновая регистрация главных категорий"""

    model = MainCategoryQuestionnaire
    extra = 0


@register(Questionnaire)
class QuestionnaireAdmin(BaseAdminMixin, ModelAdmin):
    """
    Анкеты
    """

    list_display = (
        "id",
        "name",
        "status",
    )
    inlines = [
        MainCategoryQuestionnaireInline,
    ]


class CategoryQuestionnaireInline(TabularInline):
    """Инлайновая категории"""

    model = CategoryQuestionnaire
    extra = 0
    raw_id_fields = (
        "reference_category",
        "periodicity",
        "main_category",
        "parent",
        "rating",
    )


@register(MainCategoryQuestionnaire)
class MainCategoryQuestionnaireAdmin(
    ImportExportMixin, BaseAdminMixin, ModelAdmin
):
    """
    Главная категория
    """

    raw_id_fields = (
        "reference_category",
        "questionnaire",
    )

    list_display = (
        "questionnaire",
        "number",
        "reference_category",
    )
    inlines = [
        CategoryQuestionnaireInline,
    ]

    def get_queryset(self, request):
        queryset = (
            super()
            .get_queryset(request)
            .select_related(
                "questionnaire",
                "reference_category",
            )
            .all()
        )
        return queryset


@register(CategoryQuestionnaire)
class CategoryQuestionnaireAdmin(
    ImportExportMixin, BaseAdminMixin, ModelAdmin
):
    """
    Категория анкеты
    """

    search_fields = ["reference_category__name", "pk"]
    list_filter = (
        "type_category",
        "periodicity",
    )
    list_display = (
        "pk",
        "number",
        "reference_category",
    )
    raw_id_fields = (
        # "reference_category",
        # "periodicity",
        # "main_category",
        # "parent",
        # "rating",
    )

    def get_queryset(self, request):
        queryset = (
            super()
            .get_queryset(request)
            .select_related(
                "reference_category__description",
                "periodicity",
                "main_category__reference_category",
                "main_category__questionnaire",
                "rating",
            )
            .all()
        )
        return queryset

    # функция которая изменяет queryset при выводе родительских категорий в админке, это для того чтобы заполнять анкету. Да, костыль. После заполнения закомментировать
    def render_change_form(self, request, context, *args, **kwargs):
        context["adminform"].form.fields[
            "parent"
        ].queryset = CategoryQuestionnaire.objects.filter(
            Q(main_category__questionnaire_id=4)
            | Q(parent__main_category__questionnaire_id=4)
            | Q(parent__parent__main_category__questionnaire_id=4)
        )
        return super(CategoryQuestionnaireAdmin, self).render_change_form(
            request, context, *args, **kwargs
        )


@register(QuestionnaireUser)
class QuestionnaireUserAdmin(ImportExportMixin, BaseAdminMixin, ModelAdmin):
    """
    Анкеты пользователей
    """

    list_display = (
        "user_position",
        "questionnaire",
    )

    search_fields = ["user_position__user__username"]

    # list_select_related = (
    #     "user_position__user",
    #     "user_position__department__faculty",
    #     "user_position__rate",
    #     "user_position__position",
    #     "questionnaire",
    # )

    raw_id_fields = ("user_position", "questionnaire")

    def get_queryset(self, request):
        queryset = (
            super()
            .get_queryset(request)
            .select_related(
                "user_position__user",
                "user_position__department__faculty",
                "user_position__rate",
                "user_position__position",
                "questionnaire",
            )
            .all()
        )
        return queryset


@register(MainCategoryQuestionnaireUser)
class MainCategoryQuestionnaireUserAdmin(
    ImportExportMixin, BaseAdminMixin, ModelAdmin
):
    """
    Главные категории пользователей
    """

    list_display = (
        "result_point",
        "result_point_fixed",
        "main_category_questionnaire",
        "questionnaire_user",
    )

    search_fields = [
        "questionnaire_user__user_position__user__username",
    ]

    raw_id_fields = (
        "main_category_questionnaire",
        "questionnaire_user",
    )

    def get_queryset(self, request):
        queryset = (
            super()
            .get_queryset(request)
            .select_related(
                "main_category_questionnaire__reference_category",
                "main_category_questionnaire__questionnaire",
                "questionnaire_user__questionnaire",
                "questionnaire_user__user_position__user",
                "questionnaire_user__user_position__department__faculty",
                "questionnaire_user__user_position__rate",
                "questionnaire_user__user_position__position",
            )
            .all()
        )
        return queryset


class FileCategoryQuestionnaireUserInline(TabularInline):
    """Инлайновая регистрация главных категорий"""

    model = FileCategoryQuestionnaireUser
    extra = 0
    raw_id_fields = ("prize_place", "category_questionnaire", "file")


@register(CategoryQuestionnaireUser)
class CategoryQuestionnaireUserAdmin(
    ImportExportMixin, BaseAdminMixin, ModelAdmin
):
    search_fields = ["questionnaire_user__user_position__user__username"]
    list_display = (
        "pk",
        "result_point",
        "result_point_fixed",
        "is_verified",
        "questionnaire_user",
        "category_questionnaire",
    )
    raw_id_fields = ("questionnaire_user", "category_questionnaire")
    inlines = [
        FileCategoryQuestionnaireUserInline,
    ]

    def get_queryset(self, request):
        queryset = (
            super()
            .get_queryset(request)
            .select_related(
                "questionnaire_user__questionnaire",
                "questionnaire_user__user_position__user",
                "questionnaire_user__user_position__department__faculty",
                "questionnaire_user__user_position__rate",
                "questionnaire_user__user_position__position",
                "category_questionnaire__reference_category",
            )
            .all()
        )
        return queryset


@register(FileCategoryQuestionnaireUser)
class FileCategoryQuestionnaireUserAdmin(
    ImportExportMixin, BaseAdminMixin, ModelAdmin
):
    list_display = ("pk",)
    raw_id_fields = ("prize_place", "category_questionnaire", "file")
    search_fields = ["file__name"]
