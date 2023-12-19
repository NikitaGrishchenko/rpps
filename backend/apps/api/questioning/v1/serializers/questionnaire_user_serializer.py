from apps.api.questioning.models import Questionnaire, QuestionnaireUser
from apps.api.questioning.services import (
    FormationQuestionnaireInJsonFormat,
    StatisticQuestionnaire,
)
from rest_framework import serializers

# from .questionnaire_serializer import QuestionnaireSerializer
from .user_position_serializer import UserPositionSerializer


class QuestionnaireUserSerializer(serializers.ModelSerializer):
    """ Анкета пользователя """

    user_position = UserPositionSerializer(read_only=True)
    statistics = serializers.SerializerMethodField("get_statistics")
    questionnaire = serializers.SerializerMethodField("get_questionnaire")
    info = serializers.SerializerMethodField("get_info")

    class Meta:
        model = QuestionnaireUser
        fields = "__all__"

    def get_statistics(self, questionnaire_user):
        """
        Подсчет статистики для получаемой анкеты пользователя
        """

        data = StatisticQuestionnaire.execute(
            {"questionnaire_user_id": questionnaire_user.id}
        )

        return data

    def get_questionnaire(self, questionnaire_user):
        """
        Генерация списка анкеты пользователя для вывода на клиенте
        """
        data = FormationQuestionnaireInJsonFormat.execute(
            {"questionnaire_user_id": questionnaire_user.id}
        )

        return data

    def get_info(self, questionnaire_user):
        """
        Информация об анкете пользователя
        (статус, наименование)
        """

        data = {}
        data["status"] = questionnaire_user.questionnaire.status
        data["name"] = questionnaire_user.questionnaire.name

        return data

