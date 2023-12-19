from apps.api.reference.models import MainCategory
from rest_framework import serializers


class MainCategorySerializer(serializers.ModelSerializer):
    """ Главные категории """

    class Meta:
        model = MainCategory
        fields = "__all__"
