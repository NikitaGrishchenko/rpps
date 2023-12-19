from apps.api.auth.models import User, UserPosition
from apps.api.auth.services import CreateUserAndUserPosition
from apps.api.questioning.services import CreatingQuestionnaireUser
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from .user_position_serializers import UserPositionSerializers


class UserCreateSerializer(ModelSerializer):
    """ Создание нового пользователя и должностей к нему """

    user_positions = UserPositionSerializers(many=True)
    questionnaire = serializers.ListField(write_only=True)

    class Meta:
        model = User
        fields = "__all__"

    def create(self, validated_data):
        username_data = validated_data.pop("username")
        password_data = validated_data.pop("password")
        first_name_data = validated_data.pop("first_name")
        last_name_data = validated_data.pop("last_name")
        patronymic_data = validated_data.pop("patronymic")
        user_image = validated_data.pop("user_image")
        # данные для создания должностей
        user_positions_data = validated_data.pop("user_positions")
        # id анкет с которыми нужно создать связь
        questionnaire_data = validated_data.pop("questionnaire", None)
        # Вызов сервиса - создание пользователя
        user = CreateUserAndUserPosition.execute(
            {
                "username": username_data,
                "password": password_data,
                "first_name": first_name_data,
                "last_name": last_name_data,
                "user_image": user_image,
                "patronymic": patronymic_data,
                "user_positions": user_positions_data,
            }
        )

        # Вызов сервиса - создания анкеты пользователя,
        # если указана хотя бы 1 должность
        user_positions = UserPosition.objects.filter(user=user)
        if user_positions:
            for user_position in user_positions:
                CreatingQuestionnaireUser.execute(
                    {
                        "user_position_id": user_position.id,
                        "questionnaires": questionnaire_data,
                    }
                )

        return user
