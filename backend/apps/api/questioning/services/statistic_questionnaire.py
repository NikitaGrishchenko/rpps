from apps.api.questioning.models import (
    CategoryQuestionnaireUser,
    MainCategoryQuestionnaireUser,
)
from django import forms
from service_objects.services import Service
from transliterate import translit


class StatisticQuestionnaire(Service):
    """ Сервис для подсчета статистика анкеты пользователя """

    questionnaire_user_id = forms.IntegerField()

    def process(self):
        questionnaire_user_id = self.cleaned_data["questionnaire_user_id"]

        data = {}

        main_category_questionnaire_user = MainCategoryQuestionnaireUser.objects.filter(
            questionnaire_user__id=questionnaire_user_id
        )

        # подсчет баллов главных категорий
        for category in main_category_questionnaire_user:
            dict_category = {
                "name": category.main_category_questionnaire.reference_category.short_name,
                "points": self._get_main_category_questionnaire_user_point(
                    category
                ),
                "order": category.main_category_questionnaire.number,
            }
            name_field = translit(dict_category["name"], "ru", reversed=True)
            data[name_field] = dict_category

        # сумма баллов главных категорий
        data["total_score"] = {
            "name": "СУММА",
            # "name": "Σ",
            "points": self._get_sum_main_category_questionnaire_user_point(
                data
            ),
            "order": 5,
        }

        # заполненость анкеты пользователя в %
        data["fullness_percentages"] = {
            "name": "Заполненость в %",
            "points": self._fullness_questionnaire_user_percent(
                questionnaire_user_id
            ),
            "order": 6,
        }

        # заполненость анкеты пользователя (подсчет категорий)
        data["fullness"] = {
            "name": "Заполненость (подсчет категорий)",
            "points": self._fullness_questionnaire_user_count(
                questionnaire_user_id
            ),
            "order": 7,
        }

        return data

    def _get_main_category_questionnaire_user_point(self, category):
        """
        Получить балл категории анкеты пользователя,
        Если балл исправлен - вернется исправленный, иначе обычный
        """
        if category.result_point_fixed is None:
            return round(category.result_point, 2)
        return round(category.result_point_fixed, 2)

    def _get_sum_main_category_questionnaire_user_point(self, data):
        """
        Получить сумму баллов категорий анкеты пользователя
        """
        result = 0
        for key in data.values():
            result += key["points"]
        return round(result, 2)

    def _fullness_questionnaire_user_percent(self, questionnaire_user_id):
        """
        Заполненость анкеты пользователя в %
        """
        category_questionnaire_user = CategoryQuestionnaireUser.objects.filter(
            questionnaire_user__id=questionnaire_user_id
        )
        is_point_in_category = 0
        for category in category_questionnaire_user:
            if (
                category.result_point is not None
                and category.result_point != 0
                or category.result_point_fixed is not None
            ):
                is_point_in_category += 1

            result = (
                is_point_in_category * 100
            ) / category_questionnaire_user.count()

        return f"{round(result, 2)}%"

    def _fullness_questionnaire_user_count(self, questionnaire_user_id):
        """
        Заполненость анкеты пользователя (подсчет категорий)
        """
        category_questionnaire_user = CategoryQuestionnaireUser.objects.filter(
            questionnaire_user__id=questionnaire_user_id
        )
        is_point_in_category = 0
        for category in category_questionnaire_user:
            if (
                category.result_point is not None
                and category.result_point != 0
                or category.result_point_fixed is not None
            ):
                is_point_in_category += 1

        return is_point_in_category
