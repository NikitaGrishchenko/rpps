from django.urls import path
from .views import QuestionnairePrint, DepartmentXLSXPrint, AllUsersXLSXPrint

app_name = "documents"

urlpatterns = [
    path(
        "questionnaire/<int:pk_questionnaire_user>/",
        QuestionnairePrint.as_view(),
    ),
    path(
        "department/<int:pk_department>/<int:pk_questionnaire>/",
        DepartmentXLSXPrint.as_view(),
    ),
    path("all-users/<int:pk_questionnaire>/", AllUsersXLSXPrint.as_view(),),
]
