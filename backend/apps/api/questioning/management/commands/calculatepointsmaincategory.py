from tqdm import tqdm
from django.core.management.base import BaseCommand
from apps.api.questioning.services import get_points_category_questionnaire
from ...models import MainCategoryQuestionnaireUser


class Command(BaseCommand):
    """ Класс команды """

    help = "Рассчитать баллы главных категорий пользователей"

    def calculate_and_save(self, main_category_questionnaire_user):
        """
        Расчет и сохранение балла для
        Главной категории анкеты пользователя
        """
        result = 0
        for (
            category_1
        ) in (
            main_category_questionnaire_user.main_category_questionnaire.category.all()
        ):
            if category_1.type_category is not None:
                result += get_points_category_questionnaire(
                    category_1,
                    main_category_questionnaire_user.questionnaire_user,
                )
            for category_2 in category_1.childrens.all():
                if category_2.type_category is not None:
                    result += get_points_category_questionnaire(
                        category_2,
                        main_category_questionnaire_user.questionnaire_user,
                    )
                for category_3 in category_2.childrens.all():
                    if category_3.type_category is not None:
                        result += get_points_category_questionnaire(
                            category_3,
                            main_category_questionnaire_user.questionnaire_user,
                        )
        main_category_questionnaire_user.result_point = result
        main_category_questionnaire_user.save()

    def handle(self, *args, **options):
        queryset = MainCategoryQuestionnaireUser.objects.all()

        for main_category_questionnaire_user in tqdm(queryset):
            self.calculate_and_save(main_category_questionnaire_user)
