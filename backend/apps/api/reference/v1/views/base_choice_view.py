from apps.api.questioning.services import ChoiceToDictConvertor as converter
from apps.api.reference.v1.serializers import ChoiceSerializer
from rest_framework.response import Response
from rest_framework.views import APIView


class BaseChoiceView(APIView):
    """
    Базовый класс для api choices
    """

    objects = None

    def get(self, request):
        objetcs = list(converter.convert(self.objects))
        serializer = ChoiceSerializer(objetcs, many=True)
        return Response(serializer.data)
