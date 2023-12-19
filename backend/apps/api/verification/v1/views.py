from rest_framework.generics import ListAPIView, RetrieveAPIView
from apps.api.reference.models import Faculty, Department
from .serializers import VerificationFacultySerializer


class VerificationFacultyAPIList(ListAPIView):
    """
    Список факультетов для проверки
    """

    serializer_class = VerificationFacultySerializer
    queryset = Faculty.objects.all()


class VerificationFacultyAPIRetrieve(RetrieveAPIView):
    """
    Факультет для проверки
    """

    lookup_url_kwarg = "pk_faculty"
    serializer_class = VerificationFacultySerializer
    queryset = Faculty.objects.all()
