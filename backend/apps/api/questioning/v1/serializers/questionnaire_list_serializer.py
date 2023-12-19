from apps.api.questioning.models import Questionnaire
from rest_framework import serializers


class QuestionnaireListSerializer(serializers.ModelSerializer):
    """
    Основная информация о анкете
    """

    class Meta:
        model = Questionnaire
        fields = "__all__"
