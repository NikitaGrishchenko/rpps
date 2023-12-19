from apps.api.auth.models import User, UserFile
from apps.api.questioning.services import (
    UploadFileForCategoryQuestionnaireUser,
)
from apps.api.questioning.v1.serializers import (
    CategoryQuestionnaireUserUpdateSerializer,
)
from django.utils.datastructures import MultiValueDictKeyError
from rest_framework import status
from rest_framework.response import Response

# from rest_framework import generics
from rest_framework.views import APIView


class CategoryQuestionnaireUserUploadFileAPIView(APIView):
    """
    Обновление ответов на категорию анкеты пользовотеля
    """

    def patch(self, request, pk_category):
        try:
            quantity_value = request.data["quantity_value"]
        except MultiValueDictKeyError:
            quantity_value = 0
        try:
            prize_place = request.data["prize_place"]
        except MultiValueDictKeyError:
            prize_place = 0
        try:
            coefficient = request.data["coefficient"]
        except MultiValueDictKeyError:
            coefficient = 0
        try:
            internet_resource_link = request.data["internet_resource_link"]
        except MultiValueDictKeyError:
            internet_resource_link = ""
        try:
            file = request.data["file"]
        except MultiValueDictKeyError:
            file = None

        file_for_category_questionnaire_user = (
            UploadFileForCategoryQuestionnaireUser.execute(
                {
                    "pk_category": pk_category,
                    "user_id": request.user.id,
                    "name": request.data["name"],
                    "type_file": request.data["type_file"],
                    "quantity_value": quantity_value,
                    "prize_place": prize_place,
                    "coefficient": coefficient,
                    "internet_resource_link": internet_resource_link,
                },
                files=file,
            )
        )

        if file_for_category_questionnaire_user:
            return Response({"text": "The file was created successfully"})
