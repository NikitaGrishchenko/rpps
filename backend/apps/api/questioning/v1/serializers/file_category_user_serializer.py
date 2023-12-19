from apps.api.questioning.models import FileCategoryQuestionnaireUser
from rest_framework import serializers

from .file_category_questionnaire_user_serializer import (
    FileCategoryQuestionnaireUserSerializer,
)


class FileCategoryUserSerializer(serializers.ModelSerializer):
    """
    Список прикрепленных к файлу категорий анкет пользователя
    """

    category_questionnaire = FileCategoryQuestionnaireUserSerializer()

    class Meta:
        model = FileCategoryQuestionnaireUser
        fields = "__all__"
