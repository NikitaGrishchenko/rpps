from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class ReferenceConfig(AppConfig):
    """Default app config"""

    name = "apps.api.reference"
    verbose_name = _("Справочники")

    def ready(self):
        from . import signals  # noqa: F401 # pylint: disable=unused-import
