from apps.api.reference.models import Rate
from apps.api.reference.v1.serializers import RateSerializer
from rest_framework import generics
from rest_framework.permissions import AllowAny


class RateAPIList(generics.ListAPIView):
    """
    Справочник ставок
    """
    permission_classes = [AllowAny]
    serializer_class = RateSerializer
    queryset = Rate.objects.all()
