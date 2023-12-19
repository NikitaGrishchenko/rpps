from apps.api.questioning.models import QuestionnaireUser
from apps.api.questioning.v1.serializers import QuestionnaireUserSerializer
from django.shortcuts import get_object_or_404
from rest_framework import generics


class QuestionnaireUserAPIRetrive(generics.RetrieveAPIView):
    """
    Анкета пользователя
    """

    lookup_url_kwarg = "pk_questionnaire"
    serializer_class = QuestionnaireUserSerializer

    def get_object(self):
        queryset = QuestionnaireUser.objects.select_related("user_position")
        user = self.request.user
        lookup_url_kwarg = self.lookup_url_kwarg

        filter_kwargs = {
            "pk": self.kwargs[lookup_url_kwarg],
            "user_position__user": user,
        }
        obj = get_object_or_404(queryset, **filter_kwargs)

        self.check_object_permissions(self.request, obj)
        return obj
