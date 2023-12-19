from apps.api.auth.models import User, UserFile
from apps.api.questioning.models import CategoryQuestionnaireUser
from apps.api.questioning.services import (
    AttachFileForCategoryQuestionnaireUser,
)
from apps.api.questioning.v1.serializers import AttachFileSerializer
from django.utils.datastructures import MultiValueDictKeyError
from rest_framework.response import Response
from rest_framework.views import APIView


class CategoryQuestionnaireUserAttachFileAPIView(APIView):
    """
    Обновление ответов на категорию анкеты пользовотеля
    """

    def patch(self, request, pk_category):
        serializer = AttachFileSerializer(data=request.data)
        if serializer.is_valid():
            file = AttachFileForCategoryQuestionnaireUser.execute(
                {
                    "pk_category": pk_category,
                    "user_id": request.user.id,
                    "quantity_value": serializer.data["quantity_value"],
                    "prize_place": serializer.data["prize_place"],
                    "coefficient": serializer.data["coefficient"],
                    "file_id": serializer.data["file_id"],
                    "internet_resource_link": serializer.data[
                        "internet_resource_link"
                    ],
                },
            )
            if file:
                return Response({"text": "The file was created successfully"})

