from apps.api.questioning.v1.serializers import DepartmentDetailSerializer
from apps.api.reference.models import Department
from rest_framework import generics


class QuestionnaireDepartmentAPIList(generics.RetrieveAPIView):
    """
    Анкеты кафедры
    """

    lookup_url_kwarg = "pk_department"
    serializer_class = DepartmentDetailSerializer

    def get_queryset(self):
        # print(Department.objects.all().count())
        return (
            Department.objects.all()
            .prefetch_related(
                "user_positions__user",
                "user_positions__position",
                "user_positions__rate",
                "user_positions__department",
            )
            .select_related("faculty")
        )
