from apps.api.questioning.models import FileCategoryQuestionnaireUser
from apps.api.questioning.services import (
    UpdateFileForCategoryQuestionnaireUser,
)
from apps.api.questioning.v1.serializers import (
    FileCategoryQuestionnaireUserSerializer,
)
from rest_framework.response import Response
from rest_framework.views import APIView


class FileCategoryQuestionnaireUserAPIUpdate(APIView):
    """
    Обновление прикрепленного файла к категории анкеты пользователя
    """

    serializer_class = FileCategoryQuestionnaireUserSerializer
    queryset = FileCategoryQuestionnaireUser.objects.all()

    def patch(self, request, pk_file):
        file_for_category_questionnaire_user = UpdateFileForCategoryQuestionnaireUser.execute(
            {
                "pk_file": pk_file,
                "quantity_value": request.data["quantity_value"],
                "prize_place": request.data["prize_place"],
                "coefficient": request.data["coefficient"],
                "internet_resource_link": request.data[
                    "internet_resource_link"
                ],
            }
        )

        if file_for_category_questionnaire_user:
            return Response({"text": "The file was updated successfully"})
