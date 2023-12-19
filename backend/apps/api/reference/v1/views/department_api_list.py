from apps.api.reference.models import Department
from apps.api.reference.v1.serializers import DepartmentSerializer
from rest_framework import generics
from rest_framework.permissions import AllowAny


class DepartmentAPIList(generics.ListAPIView):
    """
    Справочник кафедр
    """
    permission_classes = [AllowAny]
    serializer_class = DepartmentSerializer
    queryset = Department.objects.all()
