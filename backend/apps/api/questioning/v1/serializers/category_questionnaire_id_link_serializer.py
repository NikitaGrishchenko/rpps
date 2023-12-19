from apps.api.questioning.models import CategoryQuestionnaire
from apps.api.reference.v1.serializers import CategorySerializer
from rest_framework import serializers


class CategoryQuestionnaireIdLinkSerializer(serializers.ModelSerializer):
    """Категории анкеты сериализующая id и наличие link resource"""

    reference_category = CategorySerializer()

    class Meta:
        model = CategoryQuestionnaire
        fields = [
            "id",
            "use_internet_resource_link",
            "internet_resource_link_or_doc",
            "type_category",
            "reference_category",
        ]
