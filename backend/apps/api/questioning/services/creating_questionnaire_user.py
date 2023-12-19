from apps.api.auth.models import UserPosition
from apps.api.questioning.models import (
    CategoryQuestionnaire,
    CategoryQuestionnaireUser,
    MainCategoryQuestionnaire,
    MainCategoryQuestionnaireUser,
    Questionnaire,
    QuestionnaireUser,
)
from django import forms
from django.contrib.auth import get_user_model
from django.db import connection
from django.db.models import Q
from service_objects.fields import ListField
from service_objects.services import Service


class CreatingQuestionnaireUser(Service):
    """ Сервис для создания анкеты пользователя """

    user_position_id = forms.IntegerField()
    questionnaires = ListField()

    def process(self):
        questionnaires = self.cleaned_data["questionnaires"]
        user_position_id = self.cleaned_data["user_position_id"]
        # получаем пользователя модель пользователя

        # получаем должность пользователя
        position = UserPosition.objects.get(id=user_position_id)

        # проходим по должностям пользователя и по анкетам

        for questionnaire in questionnaires:

            # создаем анкету пользователя

            try:
                questionnaire_user = QuestionnaireUser.objects.get(
                    user_position=position, questionnaire_id=questionnaire
                )

            except QuestionnaireUser.DoesNotExist:
                questionnaire_user = QuestionnaireUser.objects.create(
                    user_position=position, questionnaire_id=questionnaire
                )

            # если анкета существует создаем
            # главные категории для этой анкеты
            main_categories = MainCategoryQuestionnaire.objects.filter(
                questionnaire_id=questionnaire_user.questionnaire_id
            )

            for main_category in main_categories:
                try:
                    MainCategoryQuestionnaireUser.objects.get(
                        main_category_questionnaire=main_category,
                        questionnaire_user=questionnaire_user,
                    )
                except MainCategoryQuestionnaireUser.DoesNotExist:
                    MainCategoryQuestionnaireUser.objects.create(
                        main_category_questionnaire=main_category,
                        questionnaire_user=questionnaire_user,
                    )

            # создание всех дочерних категорий пользователя

            # получение категорий анкеты для текущей анкеты
            categories = CategoryQuestionnaire.objects.filter(
                (Q(type_category__isnull=False))
                & (
                    Q(main_category__questionnaire_id=questionnaire)
                    | Q(parent__main_category__questionnaire_id=questionnaire)
                    | Q(
                        parent__parent__main_category__questionnaire_id=questionnaire
                    )
                )
            )

            # создание категорий анкеты пользователя
            bulk_categories = []
            for category in categories:
                try:
                    CategoryQuestionnaireUser.objects.get(
                        questionnaire_user=questionnaire_user,
                        category_questionnaire=category,
                    )
                except CategoryQuestionnaireUser.DoesNotExist:
                    bulk_categories.append(
                        CategoryQuestionnaireUser(
                            questionnaire_user=questionnaire_user,
                            category_questionnaire=category,
                            result_point=0.0,
                        )
                    )

            CategoryQuestionnaireUser.objects.bulk_create(bulk_categories)

