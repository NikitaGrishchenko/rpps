from apps.api.reference.models import Banner
from apps.api.reference.v1.serializers import BannerSerializer
from rest_framework import generics


class BannerListAPIView(generics.ListAPIView):
    """
    Баннер
    """

    serializer_class = BannerSerializer
    queryset = Banner.objects.all()
