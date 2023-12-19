from apps.api.reference.models import PrizePlace
from apps.api.reference.v1.serializers import PrizePlaceSerializer
from rest_framework import generics


class PrizePlaceAPIList(generics.ListAPIView):
    """
    Призовые места
    """

    serializer_class = PrizePlaceSerializer
    queryset = PrizePlace.objects.all()
