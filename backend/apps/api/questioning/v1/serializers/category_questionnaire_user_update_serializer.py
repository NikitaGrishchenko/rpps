from apps.api.auth.v1.serializers import UserFileSerializers
from apps.api.questioning.models import (
    CategoryQuestionnaireUser,
    FileCategoryQuestionnaireUser,
)
from drf_writable_nested.serializers import NestedUpdateMixin
from rest_framework import serializers

# from apps.api.questioning.services import LoggingChangesInUserCategories


# from .category_questionnaire_id_link_serializer import (
#     CategoryQuestionnaireIdLinkSerializer,
# )
# from .file_category_questionnaire_user_serializers import (
#     FileCategoryQuestionnaireUserSerializers,
# )


# class UserFileSerializer(serializers.Serializer):
#     file = serializers.FileField()
#     name = serializers.CharField(max_length=80)
#     type_file = serializers.IntegerField()


class CategoryQuestionnaireUserUpdateSerializer(serializers.Serializer):
    """
    Обновление категории анкеты пользователя
    """
    internet_resource_link = serializers.URLField(required=False)
    coefficient = serializers.FloatField(required=False)
    quantity_value = serializers.FloatField(required=False)
    files = UserFileSerializers(many=True)

    def update(self, instance, validated_data, *args, **kwargs):
        """
        Метод обновлния категорий анкеты пользователя
        """
        instance.coefficient = validated_data.get(
            "coefficient", instance.coefficient
        )

        return instance
