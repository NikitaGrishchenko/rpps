from rest_framework import serializers
from django.db.models import Sum
from apps.api.reference.models import Faculty, Department
from apps.api.questioning.models import CategoryQuestionnaireUser


class VerificationDepartmentSerializer(serializers.ModelSerializer):
    """ Кафедры для проверки """

    points = serializers.SerializerMethodField()

    class Meta:
        model = Department
        fields = "__all__"

    def get_points(self, instance):
        """
        Суммарное количество баллов на кафедре
        """
        return CategoryQuestionnaireUser.objects.filter(
            questionnaire_user__user_position__department=instance.pk
        ).aggregate(Sum("result_point"))


class VerificationFacultySerializer(serializers.ModelSerializer):
    """ Факультеты для проверки """

    departments = VerificationDepartmentSerializer(many=True, read_only=True)

    class Meta:
        model = Faculty
        fields = "__all__"
