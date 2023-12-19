from apps.api.auth.models import User, UserFile
from apps.api.questioning.models import (
    CategoryQuestionnaireUser,
    FileCategoryQuestionnaireUser,
)
from apps.api.reference.enums import TypeCategory, TypeFile
from apps.api.reference.models import PrizePlace

# from apps.api.reference.models import Faculty
from django import forms
from importlib_metadata import files
from rest_framework import status
from rest_framework.response import Response
from service_objects.services import Service

from .recalculation_of_user_category_points import (
    RecalculationOfUserCategoryPoints,
)


class UpdateFileForCategoryQuestionnaireUser(Service):
    """
    Сервис для изменения прикрепленого документа к
    категории анкеты пользователя
    """

    pk_file = forms.IntegerField()
    quantity_value = forms.FloatField(required=False)
    prize_place = forms.FloatField(required=False)
    coefficient = forms.FloatField(required=False)
    internet_resource_link = forms.URLField(required=False)

    def process(self):

        pk_file = self.cleaned_data["pk_file"]
        quantity_value = self.cleaned_data["quantity_value"]
        prize_place = self.cleaned_data["prize_place"]
        coefficient = self.cleaned_data["coefficient"]
        internet_resource_link = self.cleaned_data["internet_resource_link"]

        try:
            file_category_questionnaire_user = FileCategoryQuestionnaireUser.objects.get(
                id=pk_file
            )
        except FileCategoryQuestionnaireUser.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        type_file = (
            file_category_questionnaire_user.category_questionnaire.category_questionnaire.type_category
        )

        if type_file == 1:
            if coefficient > 1 or coefficient <= 0:
                return Response(status=status.HTTP_400_BAD_REQUEST)
            file_category_questionnaire_user.coefficient = coefficient
        elif type_file == 2:
            try:
                new_prize_place = PrizePlace.objects.get(id=prize_place)
                file_category_questionnaire_user.prize_place = new_prize_place
            except PrizePlace.DoesNotExist:
                return Response(status=status.HTTP_400_BAD_REQUEST)
        elif type_file == 3:
            file_category_questionnaire_user.quantity_value = quantity_value
        if (
            file_category_questionnaire_user.category_questionnaire.category_questionnaire.use_internet_resource_link
        ):
            file_category_questionnaire_user.internet_resource_link = (
                internet_resource_link
            )

        file_category_questionnaire_user.save()

        category_user = file_category_questionnaire_user.category_questionnaire
        RecalculationOfUserCategoryPoints.execute(
            {"pk_category": category_user.id}
        )

        return file_category_questionnaire_user

