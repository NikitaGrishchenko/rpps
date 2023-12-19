from apps.api.questioning.models import QuestionnaireUser
from apps.api.questioning.v1.serializers import QuestionnaireUserListSerializer
from rest_framework import generics


class QuestionnaireUserAPIList(generics.ListAPIView):
    """
    Получения списка всех имеющихся анкет для пользователя
    """

    serializer_class = QuestionnaireUserListSerializer

    def get_queryset(self):
        user = self.request.user
        queryset = QuestionnaireUser.objects.filter(
            user_position__user_id=user.pk
        ).order_by("questionnaire__status")
        return queryset
