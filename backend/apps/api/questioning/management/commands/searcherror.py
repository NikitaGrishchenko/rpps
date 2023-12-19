from apps.api.auth.models import UserPosition
from apps.api.reference.models import Department, Faculty
from django.core.management.base import BaseCommand
from django.db.models.query import Prefetch
from py_linq import Enumerable
from tqdm import tqdm

from ...models import (
    CategoryQuestionnaire,
    CategoryQuestionnaireUser,
    MainCategoryQuestionnaireUser,
    QuestionnaireUser,
)


class Command(BaseCommand):
    """ Класс команды """

    help = "Итоговый отчет"

    def handle(self, *args, **options):
        """
        Обработчик команды
        """
        qus = QuestionnaireUser.objects.all()
        cqs = CategoryQuestionnaire.objects.filter(type_category__isnull=False)

        errors = []

        for qu in tqdm(qus):
            for cq in cqs:
                # list_error = []
                cqu = CategoryQuestionnaireUser.objects.filter(
                    category_questionnaire=cq, questionnaire_user=qu
                )
                # for item in cqu:

                # print(cqu)
                # СДЕЛАТЬ ТАК ЧТОБЫ ВЫВОДИЛИСЬ ВСЕ ПОВТОРЫ
                if len(cqu) > 1:
                    errors.append(
                        {"user": qu, "errors": cqu,}
                    )

        f = open("error.txt", "w")

        for error in errors:
            f.write(
                f"{error['user'].user_position}; {error['user'].user_position.user.last_name}; {error['user'].user_position.user.first_name};  {error['errors']};"
                + "\n\n"
            )
            # for e in error["errors"]:
            #     print(
            #         f"    fact: {e.result_point} fix: {e.result_point_fixed} id: {e.id} {e.category_questionnaire.number} {e.category_questionnaire.reference_category.name}"
            #     )
            #     if e.category_questionnaire.parent is not None:
            #         print(
            #             f"        Родительская: {e.category_questionnaire.parent}"
            #         )
            #     if e.category_questionnaire.main_category is not None:
            #         print(
            #             f"        Родительская: {e.category_questionnaire.main_category}"
            #         )
            # print()
