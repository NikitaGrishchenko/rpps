from rest_framework import serializers


class AttachFileSerializer(serializers.Serializer):
    quantity_value = serializers.FloatField(allow_null=True)
    prize_place = serializers.FloatField(allow_null=True)
    coefficient = serializers.FloatField(allow_null=True)
    internet_resource_link = serializers.URLField(allow_null=True)
    file_id = serializers.IntegerField()
