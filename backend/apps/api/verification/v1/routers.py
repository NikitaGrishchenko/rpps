from django.urls import path
from .views import VerificationFacultyAPIList, VerificationFacultyAPIRetrieve

app_name = "verification"

urlpatterns = [
    path("faculty/", VerificationFacultyAPIList.as_view()),
    path(
        "faculty/<int:pk_faculty>/", VerificationFacultyAPIRetrieve.as_view()
    ),
]
