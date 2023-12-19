from apps.api.questioning.models import CategoryQuestionnaireUser
from apps.api.questioning.v1.serializers import (
    CategoryQuestionnaireUserSerializer,
)
from rest_framework import generics


class CategoryQuestionnaireUserRetriveAPIView(generics.RetrieveAPIView):
    """
    Получение ответов на категорию анкеты пользовотеля
    """

    lookup_url_kwarg = "pk_category"
    serializer_class = CategoryQuestionnaireUserSerializer
    queryset = CategoryQuestionnaireUser.objects.all()
