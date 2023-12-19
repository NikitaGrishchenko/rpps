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


class DeleteFileForCategoryQuestionnaireUser(Service):
    """
    Сервис для удаления прикрепленого документа к
    категории анкеты пользователя
    """

    pk_file = forms.IntegerField()

    def process(self):

        pk_file = self.cleaned_data["pk_file"]

        try:
            file_category_questionnaire_user = FileCategoryQuestionnaireUser.objects.get(
                id=pk_file
            )
        except FileCategoryQuestionnaireUser.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        category_user_id = (
            file_category_questionnaire_user.category_questionnaire.id
        )

        file_category_questionnaire_user.delete()

        RecalculationOfUserCategoryPoints.execute(
            {"pk_category": category_user_id}
        )

        return Response(status=status.HTTP_204_NO_CONTENT)

