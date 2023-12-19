from apps.api.auth.models import UserPosition
from apps.api.questioning.models import (
    MainCategoryQuestionnaireUser,
    QuestionnaireUser,
)
from apps.api.reference.models import Department, Faculty
from django.db.models.query import Prefetch


def get_queryset(questionnaire_id):
    """ получаем queryset для дальнейшего использования """

    # questionnaire_id = self.cleaned_data["questionnaire_id"]

    prefetch_main_category_questionnaire_user = Prefetch(
        "main_category_questionnaire_user",
        queryset=MainCategoryQuestionnaireUser.objects.all(),
    )

    prefetch_questionnaire_user = Prefetch(
        "questionnaire_user",
        queryset=QuestionnaireUser.objects.filter(
            questionnaire__id=questionnaire_id
        ).prefetch_related(prefetch_main_category_questionnaire_user),
    )

    prefetch_user_positions = Prefetch(
        "user_positions",
        queryset=UserPosition.objects.filter(
            department__isnull=False
        ).prefetch_related(prefetch_questionnaire_user),
    )
    prefetch_departments = Prefetch(
        "departments",
        queryset=Department.objects.all().prefetch_related(
            prefetch_user_positions
        ),
    )
    queryset = Faculty.objects.all().prefetch_related(prefetch_departments)

    return queryset
