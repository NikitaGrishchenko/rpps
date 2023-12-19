from apps.api.auth.models import User
from apps.api.questioning.models import FileCategoryQuestionnaireUser
from apps.api.questioning.services import get_points_category_questionnaire
from django.core.management.base import BaseCommand
from requests import request
from tqdm import tqdm


class Command(BaseCommand):
    """
    Запрос к базе данных для получения информации
    """

    def handle(self, *args, **options):
        # queryset = FileCategoryQuestionnaireUser.objects.filter(
        #     category_questionnaire__category_questionnaire__id=263
        # )
        # print(queryset)
        # for item in queryset:
        #     print(item.file.user)

        # u = User.objects.get(last_name="Ванюшкина")
        # u.last_name = "Журбина (Ванюшкина)"
        # u.save()

        # print(u.last_name)

