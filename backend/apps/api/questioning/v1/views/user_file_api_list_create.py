from apps.api.auth.models import UserFile
from apps.api.questioning.v1.serializers import UserFileSerializer
from rest_framework import generics


class UserFileAPIListCreate(generics.ListCreateAPIView):
    """
    Список и создание файлов пользователя
    """

    serializer_class = UserFileSerializer

    def get_queryset(self):
        user = self.request.user
        queryset = UserFile.objects.filter(user_id=user.pk).order_by("-id")
        return queryset

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
