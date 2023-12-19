from apps.api.questioning.models import FileCategoryQuestionnaireUser
from rest_framework import serializers

from .file_category_questionnaire_serializer import (
    FileCategoryQuestionnaireSerializer,
)


class FileCategoryQuestionnaireUserSerializer(serializers.ModelSerializer):
    """
    Список категорий анкет пользователя
    """

    # category_questionnaire = FileCategoryQuestionnaireSerializer()

    class Meta:
        model = FileCategoryQuestionnaireUser
        fields = "__all__"
