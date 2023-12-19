from tqdm import tqdm
from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model


class Command(BaseCommand):
    help = "Приведение всех username в нижний регистер"

    def add_arguments(self, parser):
        parser.add_argument(
            "--save",
            action="store_true",
            help="Save MainCategoryQuestionnaireUser records",
        )

    def handle(self, *args, **options):
        user_model = get_user_model()
        users = user_model.objects.all()
        count_lowercase_username = 0

        for user in tqdm(users):
            if not user.username.islower():
                count_lowercase_username += 1
                if options["save"]:
                    user.username = user.username.lower()
                    user.save()

        if options["save"]:
            self.stdout.write(
                self.style.SUCCESS(
                    "Количество полей, приведенных к нижнему регистру: %s"
                    % count_lowercase_username
                )
            )
        else:
            self.stdout.write(
                self.style.WARNING(
                    "Количество полей, готовых к именению: %s"
                    % count_lowercase_username
                )
            )
            self.stdout.write(
                self.style.WARNING(
                    "Используйте опцию --save для создания записей"
                )
            )
