from apps.api.questioning.models import QuestionnaireUser
from rest_framework import serializers

from ...services import StatisticQuestionnaire
from .questionnaire_list_serializer import QuestionnaireListSerializer
from .user_position_serializer import UserPositionSerializer


class QuestionnaireUserListSerializer(serializers.ModelSerializer):
    """
    Основная информация для формирования списка
    Анкет  пользователя
    """

    user_position = UserPositionSerializer(read_only=True)
    questionnaire = QuestionnaireListSerializer(read_only=True)
    statistics = serializers.SerializerMethodField("get_statistics")

    def get_statistics(self, questionnaire_user):
        """Подсчет статистики для получаемой анкеты пользователя"""

        data = StatisticQuestionnaire.execute(
            {"questionnaire_user_id": questionnaire_user.id}
        )

        return data

    class Meta:
        model = QuestionnaireUser
        fields = "__all__"
