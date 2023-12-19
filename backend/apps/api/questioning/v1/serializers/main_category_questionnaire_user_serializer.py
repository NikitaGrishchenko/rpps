from apps.api.questioning.models import MainCategoryQuestionnaireUser
from rest_framework import serializers


class MainCategoryQuestionnaireUserSerializer(serializers.ModelSerializer):
    """ Главные категории анкеты пользователя """

    class Meta:
        model = MainCategoryQuestionnaireUser
        fields = "__all__"
