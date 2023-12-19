from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class VerificationConfig(AppConfig):
    """Default app config"""

    name = "apps.api.verification"
    verbose_name = _("Verification")

    def ready(self):
        from . import signals  # noqa: F401 # pylint: disable=unused-import
