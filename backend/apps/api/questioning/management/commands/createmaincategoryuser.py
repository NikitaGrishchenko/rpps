from django.core.management.base import BaseCommand
from tqdm import tqdm

from ...models import MainCategoryQuestionnaireUser, QuestionnaireUser


class Command(BaseCommand):
    """ Класс команды """

    help = "Создание главных категорий для всех пользователей"

    def add_arguments(self, parser):
        parser.add_argument(
            "--save",
            action="store_true",
            help="Save MainCategoryQuestionnaireUser records",
        )

    def handle(self, *args, **options):
        questionnaires_users = QuestionnaireUser.objects.all()
        count_ready_questionnaires_users = 0
        new_records = []

        for questionnaire_user in tqdm(questionnaires_users):
            if not MainCategoryQuestionnaireUser.objects.filter(
                questionnaire_user=questionnaire_user
            ):
                count_ready_questionnaires_users += 1
                for (
                    main_category
                ) in questionnaire_user.questionnaire.main_category.all():
                    new_records.append(
                        MainCategoryQuestionnaireUser(
                            main_category_questionnaire=main_category,
                            questionnaire_user=questionnaire_user,
                        )
                    )

        if options["save"]:
            MainCategoryQuestionnaireUser.objects.bulk_create(new_records)
            self.stdout.write(
                self.style.SUCCESS(
                    "Количество созданных записей: %s" % len(new_records)
                )
            )
        else:
            self.stdout.write(
                self.style.SUCCESS(
                    "Количество анкет пользователя: %s"
                    % count_ready_questionnaires_users
                )
            )
            self.stdout.write(
                self.style.SUCCESS(
                    "Количество записей готовых к соданию: %s"
                    % len(new_records)
                )
            )
            self.stdout.write(
                self.style.WARNING(
                    "Используйте опцию --save для создания записей"
                )
            )
