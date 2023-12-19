# from apps.api.auth.models import UserPosition

from apps.api.auth.models import User, UserFile
from apps.api.questioning.models import (
    CategoryQuestionnaireUser,
    FileCategoryQuestionnaireUser,
)
from apps.api.reference.enums import TypeCategory, TypeFile
# from apps.api.reference.models import Faculty
from django import forms
from importlib_metadata import files
from rest_framework import status
from rest_framework.response import Response
from service_objects.services import Service


class RecalculationOfUserCategoryPoints(Service):
    """ Сервис для перерасчета баллов категории пользователя """

    pk_category = forms.IntegerField()

    def process(self):
        pk_category = self.cleaned_data["pk_category"]

        try:
            categor_questionnaire_user = CategoryQuestionnaireUser.objects.get(
                id=pk_category
            )
        except CategoryQuestionnaireUser.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        type_category = (
            categor_questionnaire_user.category_questionnaire.type_category
        )
        if type_category == 1:
            points_summ = 0
            weight = categor_questionnaire_user.category_questionnaire.weight
            max_weight = (
                categor_questionnaire_user.category_questionnaire.max_weight
            )
            for file in categor_questionnaire_user.files.all():
                points_summ += weight * file.coefficient
            if max_weight is not None:
                if points_summ > max_weight:
                    points_summ = max_weight
            categor_questionnaire_user.result_point = points_summ
            categor_questionnaire_user.save()
        elif type_category == 3:
            points_summ = 0
            weight = categor_questionnaire_user.category_questionnaire.weight

            max_weight = (
                categor_questionnaire_user.category_questionnaire.max_weight
            )
            for file in categor_questionnaire_user.files.all():
                points_summ += weight * file.quantity_value
            if max_weight is not None:
                if points_summ > max_weight:
                    points_summ = max_weight
            categor_questionnaire_user.result_point = points_summ
            categor_questionnaire_user.save()
        elif type_category == 2:
            points_summ = 0
            for file in categor_questionnaire_user.files.all():
                points_summ += file.prize_place.points
            categor_questionnaire_user.result_point = points_summ
            categor_questionnaire_user.save()

        return categor_questionnaire_user
