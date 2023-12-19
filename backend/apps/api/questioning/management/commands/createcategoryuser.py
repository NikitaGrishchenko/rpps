from django.core.management.base import BaseCommand
from tqdm import tqdm

from ...models import (
    CategoryQuestionnaire,
    CategoryQuestionnaireUser,
    QuestionnaireUser,
)


class Command(BaseCommand):
    """ Класс команды """

    help = (
        "Создать все CategoryQuestionnaireUser для"
        " CategoryQuestionnaireUser и CategoryQuestionnaire"
    )

    def handle(self, *args, **options):
        categoryes = CategoryQuestionnaire.objects.filter(
            type_category__isnull=False
        )
        questionnaires_user = QuestionnaireUser.objects.all()
        for questionnaire_user in tqdm(questionnaires_user):
            bulk_list = []
            for category in categoryes:
                try:
                    exist = CategoryQuestionnaireUser.objects.get(
                        questionnaire_user=questionnaire_user,
                        category_questionnaire=category,
                    )
                except Exception:
                    exist = None
                if exist is None:
                    bulk_list.append(
                        CategoryQuestionnaireUser(
                            questionnaire_user=questionnaire_user,
                            category_questionnaire=category,
                            result_point=0.0,
                        )
                    )
            CategoryQuestionnaireUser.objects.bulk_create(bulk_list)
