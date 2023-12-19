from apps.api.questioning.models import MainCategoryQuestionnaireUser
from apps.api.questioning.v1.serializers import (
    MainCategoryQuestionnaireUserSerializer,
)
from rest_framework import generics


class MainCategoryQuestionnaireUserAPIUpdate(generics.UpdateAPIView):
    """

    """

    serializer_class = MainCategoryQuestionnaireUserSerializer
    queryset = MainCategoryQuestionnaireUser.objects.all()
