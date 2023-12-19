from apps.api.questioning.models import MainCategoryQuestionnaire
from apps.api.reference.v1.serializers import MainCategorySerializer
from rest_framework import serializers

from .category_questionnaire_serializer import CategoryQuestionnaireSerializer
from .main_category_questionnaire_user_serializer import (
    MainCategoryQuestionnaireUserSerializer,
)


class MainCategoryQuestionnaireSerializer(serializers.ModelSerializer):
    """ Главные категории анкеты """

    category = CategoryQuestionnaireSerializer(read_only=True, many=True)
    reference_category = MainCategorySerializer()
    main_category_questionnaire_user = MainCategoryQuestionnaireUserSerializer(
        read_only=True, many=True
    )

    class Meta:
        model = MainCategoryQuestionnaire
        fields = "__all__"
