from apps.api.questioning.services import get_points_category_questionnaire
from django.core.management.base import BaseCommand
from tqdm import tqdm

from ...models import (
    CategoryQuestionnaire,
    CategoryQuestionnaireUser,
    MainCategoryQuestionnaireUser,
    QuestionnaireUser,
)


class Command(BaseCommand):
    """ Класс команды """

    help = ""

    def handle(self, *args, **options):
        # tmp = CategoryQuestionnaireUser.objects.get(id=92598)

        # print(tmp.files.all())

        # cq = CategoryQuestionnaire.objects.filter(type_category__isnull=False)
        # qu = QuestionnaireUser.objects.all()

        # count = 0

        # for questionnaire_user in qu:
        #     for category_questionnaire in cq:
        #         cqu = CategoryQuestionnaireUser.objects.filter(
        #             questionnaire_user=questionnaire_user,
        #             category_questionnaire=category_questionnaire,
        #         )
        #         if len(cqu) > 1:
        #             count += 1
        #             for item in cqu:
        #                 print(
        #                     f"{item.result_point} ==== {item.result_point_fixed} id: {item.id}"
        #                 )
        #             print("________")
        # print(count)
        cqu = CategoryQuestionnaireUser.objects.filter(
            questionnaire_user_id=4449, category_questionnaire_id=58,
        )
        for item in cqu:
            print(
                f"{item.result_point} ==== {item.result_point_fixed} id: {item.id}"
            )
        print("________")

        # main_categories_questionnaire_user = MainCategoryQuestionnaireUser.objects.filter(
        #     questionnaire_user_id=4449
        # )
        # for mcqu in main_categories_questionnaire_user:
        #     if mcqu.result_point_fixed is None:
        #         result = 0
        #         for (
        #             category_1
        #         ) in mcqu.main_category_questionnaire.category.all():
        #             if category_1.type_category is not None:
        #                 result += get_points_category_questionnaire(
        #                     category_1, mcqu.questionnaire_user
        #                 )
        #                 print(
        #                     f"{get_points_category_questionnaire( category_1, mcqu.questionnaire_user)}--{category_1.id}"
        #                 )
        #             for category_2 in category_1.childrens.all():
        #                 if category_2.type_category is not None:
        #                     result += get_points_category_questionnaire(
        #                         category_2, mcqu.questionnaire_user
        #                     )
        #                     print(
        #                         f"{get_points_category_questionnaire(category_2, mcqu.questionnaire_user)}--{category_2.id}"
        #                     )
        #                 for category_3 in category_2.childrens.all():
        #                     if category_3.type_category is not None:
        #                         result += get_points_category_questionnaire(
        #                             category_3, mcqu.questionnaire_user
        #                         )
        #                         print(
        #                             f"{get_points_category_questionnaire(category_3, mcqu.questionnaire_user)}--{category_3.id}"
        #                         )
        #                     for category_4 in category_3.childrens.all():
        #                         if category_4.type_category is not None:
        #                             result += get_points_category_questionnaire(
        #                                 category_4, mcqu.questionnaire_user
        #                             )
        #                             print(
        #                                 f"{get_points_category_questionnaire(category_4, mcqu.questionnaire_user)}--{category_4.id}"
        #                             )
        #         print(f"{mcqu.result_point} -- {result}")
        # mcqu.result_point = result
        # mcqu.save()

        # main_categories_questionnaire_user = (
        #     MainCategoryQuestionnaireUser.objects.all()
        # )
        # for mcqu in tqdm(main_categories_questionnaire_user):
        #     if mcqu.result_point_fixed is None:
        #         result = 0
        #         for (
        #             category_1
        #         ) in mcqu.main_category_questionnaire.category.all():
        #             if category_1.type_category is not None:
        #                 result += get_points_category_questionnaire(
        #                     category_1, mcqu.questionnaire_user
        #                 )
        #             for category_2 in category_1.childrens.all():
        #                 if category_2.type_category is not None:
        #                     result += get_points_category_questionnaire(
        #                         category_2, mcqu.questionnaire_user
        #                     )
        #                 for category_3 in category_2.childrens.all():
        #                     if category_3.type_category is not None:
        #                         result += get_points_category_questionnaire(
        #                             category_3, mcqu.questionnaire_user
        #                         )
        #         mcqu.result_point = result
        #         mcqu.save()
