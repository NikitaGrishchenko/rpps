from apps.api.reference.models import Faculty
from rest_framework import serializers

from .department_serializer import DepartmentSerializer


class FacultySerializer(serializers.ModelSerializer):
    """ Факультет """

    departments = DepartmentSerializer(many=True, read_only=True)

    class Meta:
        model = Faculty
        fields = "__all__"
