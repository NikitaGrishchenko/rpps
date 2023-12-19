from apps.api.questioning.models import QuestionnaireUser
from apps.api.questioning.v1.serializers import (
    QuestionnaireUserListAPISerializer,
)
from rest_framework import generics


class ConfirmEffectiveContract(generics.RetrieveUpdateAPIView):
    serializer_class = QuestionnaireUserListAPISerializer
    queryset = QuestionnaireUser.objects.all()
