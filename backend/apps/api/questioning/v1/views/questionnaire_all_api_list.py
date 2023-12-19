from apps.api.questioning.models import Questionnaire
from apps.api.questioning.v1.serializers import (
    QuestionnaireNameAndIdSerializer,
)
from rest_framework import generics


class QuestionnaireAllAPIList(generics.ListAPIView):
    """
    Список всех имеющихся анкет
    """

    serializer_class = QuestionnaireNameAndIdSerializer
    queryset = Questionnaire.objects.all()
