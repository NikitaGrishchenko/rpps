from rest_framework import serializers


class ChoiceSerializer(serializers.Serializer):
    """
    Сериализатор перечислений
    """

    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=100)
