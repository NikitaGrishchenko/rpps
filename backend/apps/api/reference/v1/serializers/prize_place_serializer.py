from apps.api.reference.models import PrizePlace
from rest_framework import serializers


class PrizePlaceSerializer(serializers.ModelSerializer):
    """ Призовое место """

    class Meta:
        model = PrizePlace
        fields = "__all__"
