from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class QuestioningConfig(AppConfig):
    """Default app config"""

    name = "apps.api.questioning"
    verbose_name = _("Анкетирование")

    def ready(self):
        from . import signals  # noqa: F401 # pylint: disable=unused-import
