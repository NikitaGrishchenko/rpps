from apps.api.questioning.models import FileCategoryQuestionnaireUser
from apps.api.questioning.v1.serializers import (
    FileCategoryQuestionnaireUserSerializers,
)
from rest_framework import generics


class FileCategoryQuestionnaireUserRetrieveAPIView(generics.RetrieveAPIView):
    """
    Получение прикрепленного файла пользователя
    """

    lookup_url_kwarg = "pk_file"
    serializer_class = FileCategoryQuestionnaireUserSerializers
    queryset = FileCategoryQuestionnaireUser.objects.all()
