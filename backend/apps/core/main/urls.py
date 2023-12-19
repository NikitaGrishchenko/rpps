from django.conf.urls import url
from django.urls import include, path, re_path, reverse, reverse_lazy

# from .views import IndexRedirectView
from django.views.generic.base import RedirectView

urlpatterns = [
    path("api/", include("apps.core.api.urls")),
    path("api-auth/", include("rest_framework.urls")),
    path("", RedirectView.as_view(pattern_name="admin:index"), name="index"),
]
