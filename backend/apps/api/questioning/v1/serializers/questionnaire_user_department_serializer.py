from apps.api.questioning.models import QuestionnaireUser
from rest_framework import serializers

from .questionnaire_list_serializer import QuestionnaireListSerializer


class QuestionnaireUserDepartmentSerializer(serializers.ModelSerializer):
    """ Анкета пользователя """

    questionnaire = QuestionnaireListSerializer(read_only=True)

    class Meta:
        model = QuestionnaireUser
        fields = "__all__"
