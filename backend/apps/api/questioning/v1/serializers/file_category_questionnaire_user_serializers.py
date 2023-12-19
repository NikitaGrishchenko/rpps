from apps.api.auth.v1.serializers import UserFileSerializers
from apps.api.questioning.models import FileCategoryQuestionnaireUser
from apps.api.reference.v1.serializers import PrizePlaceSerializer
from rest_framework import serializers

from .category_questionnaire_id_link_serializer import (
    CategoryQuestionnaireIdLinkSerializer,
)


class FileCategoryQuestionnaireUserSerializers(serializers.ModelSerializer):
    """ Файлы Категорий анкеты пользовотеля """

    url = serializers.CharField(source="file.file", read_only=True)
    file = UserFileSerializers()
    prize_place = PrizePlaceSerializer()

    class Meta:
        model = FileCategoryQuestionnaireUser
        fields = "__all__"
