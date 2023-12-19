from apps.api.questioning.models import FileCategoryQuestionnaireUser
from apps.api.questioning.services import (
    DeleteFileForCategoryQuestionnaireUser,
    UpdateFileForCategoryQuestionnaireUser,
)
from apps.api.questioning.v1.serializers import (
    FileCategoryQuestionnaireUserSerializer,
)
from django.utils.datastructures import MultiValueDictKeyError
from rest_framework.response import Response
from rest_framework.views import APIView


class FileCategoryQuestionnaireUserAPIDelete(APIView):
    """
    Удаление прикрепленного файла к категории анкеты пользователя
    """

    serializer_class = FileCategoryQuestionnaireUserSerializer
    queryset = FileCategoryQuestionnaireUser.objects.all()

    def delete(self, request, pk_file):
        response = DeleteFileForCategoryQuestionnaireUser.execute(
            {"pk_file": pk_file,}
        )

        return response
