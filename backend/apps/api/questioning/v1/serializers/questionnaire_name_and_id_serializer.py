from apps.api.questioning.models import Questionnaire
from rest_framework import serializers


class QuestionnaireNameAndIdSerializer(serializers.ModelSerializer):
    """ Сериализатор имени и id анкеты (без дочерних элементов)
    для регистрации пользователя """

    class Meta:
        model = Questionnaire
        fields = ("id", "name")
