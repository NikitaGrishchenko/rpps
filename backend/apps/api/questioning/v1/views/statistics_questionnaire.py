from apps.api.questioning.services import QuestionnaireStatistics
from rest_framework.response import Response
from rest_framework.views import APIView


class StatisticsQuestionnaire(APIView):
    """ Статистика по выбранной анкете """

    lookup_url_kwarg = "pk"

    def get(self, request, *args, **kwargs):

        pk_questionnaire = self.kwargs["pk"]

        data = QuestionnaireStatistics.execute(
            {"questionnaire_id": pk_questionnaire}
        )

        # results = StatisticsQuestionnaire(data, many=True).data

        return Response(data)
