from apps.api.questioning.services import CreatingQuestionnaireUser
from rest_framework import serializers


class CreatingQuestionnairesUsers(serializers.Serializer):
    """ Массовое создание анкет и категорий для должностей пользователя """

    user_positions = serializers.ListField(write_only=True)
    questionnaires_users = serializers.ListField(write_only=True)

    def create(self, validated_data):
        user_positions = validated_data.pop("user_positions", None)
        questionnaires_users = validated_data.pop("questionnaires_users", None)

        if user_positions and questionnaires_users:
            for user_position in user_positions:
                CreatingQuestionnaireUser.execute(
                    {
                        "user_position_id": user_position,
                        "questionnaires": questionnaires_users,
                    }
                )

        return validated_data
