from apps.api.questioning.models import CategoryQuestionnaire
from apps.api.reference.v1.serializers import CategorySerializer
from rest_framework import serializers


class FileCategoryQuestionnaireSerializer(serializers.ModelSerializer):
    """
    Категории анкеты
    """

    reference_category = CategorySerializer()

    class Meta:
        model = CategoryQuestionnaire
        fields = "__all__"
