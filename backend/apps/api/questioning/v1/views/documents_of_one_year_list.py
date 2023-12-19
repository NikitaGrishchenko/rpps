from apps.api.auth.models import UserFile
from apps.api.questioning.v1.serializers import UserFileSerializer
from rest_framework import generics
from rest_framework.response import Response


class DocumentsOfOneYearList(generics.ListAPIView):
    """ Список документов пользователя для выбранного года """

    lookup_url_kwarg = "year"
    serializer_class = UserFileSerializer

    def get_queryset(self):
        user = self.request.user
        queryset = UserFile.objects.filter(user_id=user.pk).order_by(
            "-date_upload"
        )
        return queryset

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        response_list = serializer.data
        year = self.kwargs["year"]
        list_result = []
        for item in response_list:
            if (int(item["date_upload"][6:10])) == int(year):
                list_result.append(item)
        return Response(list_result)
