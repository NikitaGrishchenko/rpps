from apps.api.questioning.models import QuestionnaireUser
from rest_framework import serializers

from .questionnaire_list_serializer import QuestionnaireListSerializer


class QuestionnaireUserListAPISerializer(serializers.ModelSerializer):
    """
    Основная информация для формирования списка
    Анкет пользователя без должности
    """

    questionnaire = QuestionnaireListSerializer(read_only=True)

    class Meta:
        model = QuestionnaireUser
        fields = "__all__"
