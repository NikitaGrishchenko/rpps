from django.db import models


class CommonUsersManager(models.Manager):
    """
    Обычные пользователи
    """

    def get_queryset(self):
        return (
            super()
            .get_queryset()
            .filter(
                is_manager_faculty=False,
                is_manager_department=False,
                is_expert=False,
                is_super_expert=False,
            )
        )
