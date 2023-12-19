from apps.api.auth.models import UserFile
from rest_framework import serializers

from .file_category_user_serializer import FileCategoryUserSerializer


class UserFileSerializer(serializers.ModelSerializer):
    """ Файл пользователя """

    file_category_questionnaire_user = FileCategoryUserSerializer(
        many=True, read_only=True
    )

    class Meta:
        model = UserFile
        fields = "__all__"
