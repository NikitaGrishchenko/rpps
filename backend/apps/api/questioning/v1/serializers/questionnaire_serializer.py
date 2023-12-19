from apps.api.questioning.models import Questionnaire
from rest_framework import serializers

from .main_category_questionnaire_serializer import (
    MainCategoryQuestionnaireSerializer,
)


class QuestionnaireSerializer(serializers.ModelSerializer):
    """ Анкета """

    main_category = MainCategoryQuestionnaireSerializer(
        read_only=True, many=True
    )

    class Meta:
        model = Questionnaire
        fields = "__all__"

