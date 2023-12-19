from apps.api.auth.v1.serializers import UserFileSerializers
from apps.api.questioning.models import (
    CategoryQuestionnaireUser,
    FileCategoryQuestionnaireUser,
)

# from apps.api.questioning.services import LoggingChangesInUserCategories
# from django.forms import IntegerField
from drf_writable_nested.serializers import NestedUpdateMixin
from rest_framework import serializers

from .category_questionnaire_id_link_serializer import (
    CategoryQuestionnaireIdLinkSerializer,
)
from .file_category_questionnaire_user_serializers import (
    FileCategoryQuestionnaireUserSerializers,
)


class CategoryQuestionnaireUserSerializer(serializers.ModelSerializer):
    """
    Сериализатор категории анкеты пользователя
    """

    files = serializers.SerializerMethodField()
    category_questionnaire = CategoryQuestionnaireIdLinkSerializer()

    def get_files(self, category_questionnaire_user):
        """
        Получение всех файлов пользователя для данной категории пользователя
        """
        queryset = FileCategoryQuestionnaireUser.objects.filter(
            category_questionnaire=category_questionnaire_user
        ).order_by("-file__date_upload")

        serializer = FileCategoryQuestionnaireUserSerializers(
            instance=queryset, many=True
        )
        return serializer.data

    class Meta:
        model = CategoryQuestionnaireUser
        fields = "__all__"
