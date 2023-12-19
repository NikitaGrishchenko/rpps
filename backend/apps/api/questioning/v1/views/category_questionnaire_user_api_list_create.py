from apps.api.questioning.models import CategoryQuestionnaireUser
from apps.api.questioning.v1.serializers import (
    CategoryQuestionnaireUserSerializer,
)
from rest_framework import generics


class CategoryQuestionnaireUserAPIListCreate(generics.ListCreateAPIView):
    """
    Добавление категории (ответов) анкеты пользовотеля
    """

    serializer_class = CategoryQuestionnaireUserSerializer
    queryset = CategoryQuestionnaireUser.objects.all()

    def perform_create(self, serializer):
        serializer.save()
