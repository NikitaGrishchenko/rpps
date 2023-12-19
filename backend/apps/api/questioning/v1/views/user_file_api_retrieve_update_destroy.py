from apps.api.auth.models import UserFile
from apps.api.questioning.v1.serializers import UserFileSerializer
from rest_framework import generics


class UserFileAPIRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    """
    Обновление, удаление, детальная информация
    Файлов пользователя
    """

    serializer_class = UserFileSerializer
    queryset = UserFile.objects.all()
