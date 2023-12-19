from datetime import datetime

from apps.api.auth.models import UserFile
from apps.api.questioning.v1.serializers import UserFileSerializer
from rest_framework import generics
from rest_framework.response import Response


class AllYearsOfUserDocumentsList(generics.ListAPIView):
    """ Список всех годов у имеющихся документов пользователя """

    serializer_class = UserFileSerializer

    def get_queryset(self):
        user = self.request.user
        queryset = UserFile.objects.filter(user_id=user.pk)
        return queryset

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        response_list = serializer.data
        currentYear = str(datetime.now().year)
        years_all = []
        for item in response_list:
            years_all.append(item["date_upload"][6:10])
        # Добавление текущего года, если такового нет в списке
        if currentYear not in years_all:
            years_all.append(currentYear)
        # Сортировка списка годов по убыванию
        years_result = sorted(list(set(years_all)), key=int, reverse=True)
        return Response(years_result)
