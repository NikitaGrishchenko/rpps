from tqdm import tqdm
from django.core.management.base import BaseCommand
from apps.api.questioning.services import get_result_questionnaire_user
from django.contrib.auth import get_user_model
from apps.api.questioning.models import (
    CategoryQuestionnaire,
    CategoryQuestionnaireUser,
    QuestionnaireUser,
)


class Command(BaseCommand):
    help = "Песочница"

    def handle(self, *args, **options):
        qu = QuestionnaireUser.objects.get(id=4816)
        result = get_result_questionnaire_user(qu)

        print(result)
        # #
        # fail_id = [42, 43, 45, 46, 48, 49, 51, 52]

        # categories = (
        #     CategoryQuestionnaireUser.objects.all()
        #     .filter(category_questionnaire_id__in=fail_id)
        #     .order_by("category_questionnaire_id")
        # )
        # print(f"Всего: {len(categories)}")
        # for category_user in categories:
        #     print(
        #         f"Категория пользователя: {category_user.id}, Категория: {category_user.category_questionnaire_id} (тип: {category_user.category_questionnaire.type_category})"
        #     )
