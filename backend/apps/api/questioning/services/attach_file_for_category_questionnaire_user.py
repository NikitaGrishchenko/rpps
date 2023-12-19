from apps.api.auth.models import User, UserFile
from apps.api.questioning.models import (
    CategoryQuestionnaireUser,
    FileCategoryQuestionnaireUser,
)
from apps.api.reference.enums import TypeFile
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


class AttachFileForCategoryQuestionnaireUser(Service):
    """
    Logic for attach user file to category questionnaire user

    Arguments:
      quantity_value
      prize_place
      coefficient
      internet_resource_link
      file_id

    Returns:

    """

    pk_category = forms.IntegerField()
    user_id = forms.IntegerField()
    quantity_value = forms.FloatField(required=False)
    prize_place = forms.FloatField(required=False)
    coefficient = forms.FloatField(required=False)
    internet_resource_link = forms.URLField(required=False)
    file_id = forms.IntegerField()

    def process(self):

        pk_category = self.cleaned_data["pk_category"]
        user_id = self.cleaned_data["user_id"]
        quantity_value = self.cleaned_data["quantity_value"]
        prize_place = self.cleaned_data["prize_place"]
        coefficient = self.cleaned_data["coefficient"]
        internet_resource_link = self.cleaned_data["internet_resource_link"]
        file_id = self.cleaned_data["file_id"]

        try:
            categor_questionnaire_user = CategoryQuestionnaireUser.objects.get(
                id=pk_category
            )
        except CategoryQuestionnaireUser.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        try:
            user = User.objects.get(id=user_id)
        except User.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        try:
            user_file = UserFile.objects.get(id=file_id)
        except UserFile.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        tp = categor_questionnaire_user.category_questionnaire.type_category

        if tp == 1 and user_file:
            if coefficient > 1 or coefficient <= 0:
                return Response(status=status.HTTP_400_BAD_REQUEST)
            file_category_questionnaire_user = self._document_type_category(
                user_file, categor_questionnaire_user, coefficient
            )
        elif tp == 2 and user_file:
            file_category_questionnaire_user = self._rating_type_category(
                user_file, categor_questionnaire_user, prize_place
            )
        elif tp == 3 and user_file:
            file_category_questionnaire_user = self._number_type_category(
                user_file, categor_questionnaire_user, quantity_value
            )

        uirl = (
            categor_questionnaire_user.category_questionnaire.use_internet_resource_link
        )

        if uirl is True and internet_resource_link != "":
            file_category_questionnaire_user = self._internet_resource_link_category(
                file_category_questionnaire_user, internet_resource_link
            )

        RecalculationOfUserCategoryPoints.execute(
            {"pk_category": categor_questionnaire_user.id}
        )

        return file_category_questionnaire_user

    def _document_type_category(
        self, user_file, categor_questionnaire_user, coefficient
    ):
        """
        """
        file_category_questionnaire_user = FileCategoryQuestionnaireUser.objects.create(
            file=user_file,
            category_questionnaire=categor_questionnaire_user,
            coefficient=coefficient,
        )
        if file_category_questionnaire_user:
            return file_category_questionnaire_user
        return Response(status=status.HTTP_400_BAD_REQUEST)

    def _number_type_category(
        self, user_file, categor_questionnaire_user, quantity_value
    ):
        """
        """
        file_category_questionnaire_user = FileCategoryQuestionnaireUser.objects.create(
            file=user_file,
            category_questionnaire=categor_questionnaire_user,
            quantity_value=quantity_value,
        )
        if file_category_questionnaire_user:
            return file_category_questionnaire_user
        return Response(status=status.HTTP_400_BAD_REQUEST)

    def _rating_type_category(
        self, user_file, categor_questionnaire_user, prize_place
    ):
        """
        """
        file_category_questionnaire_user = FileCategoryQuestionnaireUser.objects.create(
            file=user_file,
            category_questionnaire=categor_questionnaire_user,
            prize_place_id=prize_place,
        )
        if file_category_questionnaire_user:
            return file_category_questionnaire_user
        return Response(status=status.HTTP_400_BAD_REQUEST)

    def _internet_resource_link_category(
        self, file_category_questionnaire_user, internet_resource_link
    ):
        """
        """
        file_category_questionnaire_user.internet_resource_link = (
            internet_resource_link
        )
        file_category_questionnaire_user.save()

        return file_category_questionnaire_user

