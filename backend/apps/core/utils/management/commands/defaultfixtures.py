from django.conf import settings
from django.core import management
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    """Command create django app"""

    help = (
        "Creates a Django app directory structure"
        " for the given app name in the apps directory."
    )

    def handle(self, *args, **options):
        for name in settings.DEFAULT_FIXTURES:
            management.call_command("loaddata", name)
