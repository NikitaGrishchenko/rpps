from apps.api.reference.models import Position
from apps.api.reference.v1.serializers import DepartmentSerializer
from rest_framework import generics
from rest_framework.permissions import AllowAny


class PositionAPIList(generics.ListAPIView):
    """
    Справочник должностей
    """
    permission_classes = [AllowAny]
    serializer_class = DepartmentSerializer
    queryset = Position.objects.all()
