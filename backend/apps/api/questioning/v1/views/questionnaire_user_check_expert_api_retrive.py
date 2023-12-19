from apps.api.questioning.models import QuestionnaireUser
from apps.api.questioning.v1.serializers import QuestionnaireUserSerializer
from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework.permissions import BasePermission, IsAuthenticated


class ExpertPermissions(BasePermission):
    def has_permission(self, request, view):
        if (
            request.user.is_manager_department
            or request.user.is_manager_faculty
            or request.user.is_expert
            or request.user.is_super_expert
            or request.user.is_superuser
        ):
            return True
        return False


class QuestionnaireUserCheckExpertAPIRetrive(generics.RetrieveAPIView):
    """
    Анкета пользователя для эксперта
    """

    lookup_url_kwarg = "pk_questionnaire"
    serializer_class = QuestionnaireUserSerializer
    permission_classes = [IsAuthenticated & ExpertPermissions]

    def get_object(self):
        queryset = QuestionnaireUser.objects.select_related("user_position")
        lookup_url_kwarg = self.lookup_url_kwarg

        filter_kwargs = {
            "pk": self.kwargs[lookup_url_kwarg],
        }
        obj = get_object_or_404(queryset, **filter_kwargs)

        self.check_object_permissions(self.request, obj)

        return obj
