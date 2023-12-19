from apps.api.auth.models import UserFile
from rest_framework import serializers

from .file_category_user_serializer import FileCategoryUserSerializer


class UserFileSelectSerializer(serializers.ModelSerializer):
    """
    Список файлов пользователя для выпадаюзего меню
    fileds: id, name
    """

    class Meta:
        model = UserFile
        fields = ("id", "name")
