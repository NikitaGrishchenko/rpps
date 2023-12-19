from apps.api.questioning.models import CategoryQuestionnaire
from apps.api.reference.v1.serializers import CategorySerializer
from rest_framework import serializers
from rest_framework_recursive.fields import RecursiveField

from .category_questionnaire_user_serializer import (
    CategoryQuestionnaireUserSerializer,
)


class CategoryQuestionnaireSerializer(serializers.ModelSerializer):
    """ Категории анкеты """

    reference_category = CategorySerializer()
    childrens = RecursiveField(required=False, allow_null=True, many=True)
    category_questionnaire_user = CategoryQuestionnaireUserSerializer(
        many=True
    )

    class Meta:
        model = CategoryQuestionnaire
        fields = "__all__"
