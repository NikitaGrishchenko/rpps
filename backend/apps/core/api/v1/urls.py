from django.urls import include, path

app_name = "v1"

urlpatterns = [
    path("auth/", include("apps.api.auth.v1")),
    path("questionnaire/", include("apps.api.questioning.v1")),
    path("reference/", include("apps.api.reference.v1")),
    path("documents/", include("apps.api.documents.v1")),
    path("verification/", include("apps.api.verification.v1")),
]
