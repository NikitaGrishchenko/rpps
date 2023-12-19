from apps.api.questioning.services import StatisticsByCategory
from rest_framework.response import Response
from rest_framework.views import APIView


class StatisticsByCategoryApi(APIView):
    """ Статистика по выбранной категории анкеты """

    lookup_url_kwarg = "pk_category"

    def get(self, request, *args, **kwargs):

        pk_category = self.kwargs["pk_category"]

        data = StatisticsByCategory.execute({"pk_category": pk_category})

        return Response(data)
