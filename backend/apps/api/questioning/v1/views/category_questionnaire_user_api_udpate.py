from apps.api.questioning.models import CategoryQuestionnaireUser
from apps.api.questioning.services import RecalculationOfUserCategoryPoints
from apps.api.questioning.v1.serializers import (
    CategoryQuestionnaireUserSerializer,
)
from rest_framework import generics


class CategoryQuestionnaireUserAPIUdpate(generics.UpdateAPIView):
    """
    Редактирование значение категории анкеты пользователя
    """

    queryset = CategoryQuestionnaireUser.objects.all()
    serializer_class = CategoryQuestionnaireUserSerializer

