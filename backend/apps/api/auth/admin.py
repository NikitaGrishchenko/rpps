from apps.core.utils.admin import BaseAdminMixin
from django.contrib import admin
from django.contrib.admin import ModelAdmin
from django.contrib.auth.admin import GroupAdmin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import Group as BaseGroup
from django.utils.translation import gettext_lazy as _
from import_export.admin import ImportExportMixin, ImportExportModelAdmin

from .models import (
    ApplicationSubmission,
    ApplicationSubmissionPosition,
    ProxyGroup,
    User,
    UserFile,
    UserPosition,
)


class ApplicationSubmissionPositionInline(admin.TabularInline):
    """
    Инлайновая отправка заявки на регистрацию пользователя
    """

    model = ApplicationSubmissionPosition
    extra = 0


class UserFileInline(admin.TabularInline):
    """
    Инлайновая регистрация файла пользователя
    """

    model = UserFile
    extra = 0
    raw_id_fields = ("user",)


class UserPositionInline(admin.TabularInline):
    """
    Инлайновая регистрация
    Должности пользователя на кафедре со ставкой
    """

    model = UserPosition
    extra = 0
    raw_id_fields = ("user", "department", "rate", "position")


@admin.register(User)
class UserAdmin(ImportExportModelAdmin, BaseUserAdmin):
    list_filter = ("is_superuser",)
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        (
            _("Personal info"),
            {
                "fields": (
                    "first_name",
                    "last_name",
                    "patronymic",
                    "email",
                    "user_image",
                )
            },
        ),
        (
            _("Роль пользователя в системе"),
            {
                "fields": (
                    "is_manager_department",
                    "manager_department",
                    "is_manager_faculty",
                    "manager_faculty",
                    "is_expert",
                    "category_expert",
                    "is_super_expert",
                ),
            },
        ),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )
    list_readonly_not_superuser_fields = (
        "is_superuser",
        "is_staff",
        "last_login",
        "date_joined",
    )
    inlines = [
        UserPositionInline,
        # UserFileInline,
    ]

    # raw_id_fields = (
    #     "manager_department",
    #     "manager_faculty",
    #     "category_expert",
    # )


admin.site.unregister(BaseGroup)
admin.site.register(ProxyGroup, GroupAdmin)


@admin.register(UserFile)
class UserFileAdmin(ImportExportMixin, BaseAdminMixin, ModelAdmin):
    list_display = (
        "user",
        "name",
    )

    search_fields = ["name", "user__username"]

    def get_queryset(self, request):
        return UserFile.objects.select_related("user").all()


@admin.register(UserPosition)
class UserPositionFileAdmin(ImportExportMixin, BaseAdminMixin, ModelAdmin):
    list_display = (
        "user",
        "rate",
        "department",
        "position",
    )

    raw_id_fields = (
        "user",
        "rate",
    )

    search_fields = ["user__username", "department__name", "user__last_name"]

    def get_queryset(self, request):
        return UserPosition.objects.select_related(
            "user", "department__faculty", "rate", "position",
        ).all()


@admin.register(ApplicationSubmission)
class ApplicationSubmissionAdmin(
    ImportExportMixin, BaseAdminMixin, ModelAdmin
):

    list_display = (
        "first_name",
        "last_name",
    )

    inlines = [
        ApplicationSubmissionPositionInline,
    ]
