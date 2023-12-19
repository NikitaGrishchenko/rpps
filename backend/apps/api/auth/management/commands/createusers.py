import csv
import string
import random
from tqdm import tqdm
from transliterate import translit
from django.core.management.base import BaseCommand
from django.db.models.query import Prefetch
from django.contrib.auth import get_user_model
from apps.api.reference.models import Faculty, Department


class Command(BaseCommand):
    """
    Класс команды
    """

    help = (
        "Создание учеток деканов, и заведующих кафедры"
        + " для существующих в системе подразделений"
    )

    def add_arguments(self, parser):
        parser.add_argument(
            "--save",
            action="store_true",
            help="Save MainCategoryQuestionnaireUser records",
        )

    DEAN_LOGIN_PREFIX = "dean_"
    DEPARTMENT_LOGIN_PREFIX = "department_"

    def handle(self, *args, **options):
        user_model = get_user_model()
        faculties = Faculty.objects.all().prefetch_related(
            Prefetch("departments", queryset=Department.objects.all())
        )
        users = self.get_user_list(faculties=faculties, user_model=user_model)
        save_flag = options["save"]
        with open("users.csv", "w") as csvfile:
            filewriter = csv.writer(csvfile, delimiter=";")
            filewriter.writerow(["Login", "Password", "Кафедра/факультет"])
            for user in tqdm(users):
                self.write_and_save_user(
                    user=user, file_writer=filewriter, save_flag=save_flag
                )

    def write_and_save_user(self, user, file_writer, save_flag):
        password = self.generate_password()
        if user.is_manager_department:
            file_writer.writerow(
                [user.username, password, user.manager_department.name,]
            )
        if user.is_manager_faculty:
            file_writer.writerow(
                [user.username, password, user.manager_faculty.short_name]
            )
        if save_flag:
            user.set_password(password)
            user.save()

    def generate_password(self):
        """
        Генерация пароля
        """
        password = ""
        for __ in range(0, 6):
            password += random.choice(string.ascii_letters)
        return password.lower()

    def get_user_list(self, faculties, user_model):
        """
        Возвращает список пользователей
        """
        user_list = []
        for faculty in faculties:
            user_list.append(self.get_user_faculty(user_model, faculty))
            for department in faculty.departments.all():
                user_list.append(
                    self.get_user_department(user_model, department)
                )
        return user_list

    def get_user_faculty(self, user_model, faculty):
        """
        Создает и возвращает объект учетной записи декана
        """
        login = self.DEAN_LOGIN_PREFIX + translit(
            faculty.short_name.replace(" ", "_"), "ru", reversed=True
        )
        user = user_model()
        # user.set_password = self.generate_password()
        user.username = login.lower()
        user.is_manager_faculty = True
        user.manager_faculty = faculty
        return user

    def get_user_department(self, user_model, department):
        """
        Создает и возвращает объект учетной записи заведующего кафедрой
        """
        login = self.DEPARTMENT_LOGIN_PREFIX + translit(
            department.short_name.replace(" ", "_"), "ru", reversed=True
        )
        user = user_model()
        # user.set_password = self.generate_password()
        user.username = login.lower()
        user.is_manager_department = True
        user.manager_department = department
        return user

    def save_users(self, user_list):
        """
        Сохраняет пользователей в бд
        """

        for user in user_list:
            user.save()
