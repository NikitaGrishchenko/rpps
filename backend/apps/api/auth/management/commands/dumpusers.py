import json

from config.settings.components.paths import STATIC
from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Загрузка пользователей в базу их fixture auth_api"

    def handle(self, *args, **options):
        fixture = FIXTURES_DIR + "/auth_api.json"
        user_model = get_user_model()
        counter = 0
        with open(fixture, encoding="utf-8") as f:
            data = json.load(f)

        for user_json in data:
            fields = user_json["fields"]
            print(fields.get("password"))

            user = user_model.objects.create_user(
                fields.get("username"), password=fields.get("password"),
            )
            user.first_name = fields.get("first_name")
            user.last_name = fields.get("last_name")
            user.patronymic = fields.get("patronymic")

            user.save()
            counter = counter + 1
            print("user добавлен " + str(counter))
