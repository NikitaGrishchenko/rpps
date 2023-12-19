from enum import Enum, unique

from django.utils.translation import gettext_lazy as _
from etc.choices import ChoicesEnumMixin, get_choices


@unique
class TypeCategory(ChoicesEnumMixin, Enum):
    """
    Тип категории
    """

    # TODO: добавить содержимое перечисления

    # Весомость показателя - целое число
    # Весомость показателя - целЫое число, с учетом соавторства
    UPLOAD_DOCUMENTS = 1, _("Загрузка документов")
    # Занятые места представляют собой кол-во баллов
    RATING = 2, _("Рейтинг")
    # Умножение какой-либо величины на вес
    NUMBER_ENTRY = 3, _("Ввод числа")


@unique
class Collaborators(ChoicesEnumMixin, Enum):
    """
    Наличие соавторов
    """

    EXIST_COLLABORATORS = 1, _("Есть соавторы")
    NO_COLLABORATORS = 2, _("Нет соавторов")


@unique
class StatusQuestionnaire(ChoicesEnumMixin, Enum):
    """
    Статус анкеты
    """

    OPEN = 1, _("Анкетирование открыто")
    CLOSE = 2, _("Анкетирование закончено")


@unique
class TypeFile(ChoicesEnumMixin, Enum):
    """
    Тип Файла
    """

    GRATITUDE = 22, _("Благодарность")
    OUTPUT = 13, _("Выходные данные")
    DIPLOMA = 20, _("Грамота")
    GRANT = 18, _("Грант")
    DIPLOM = 16, _("Диплом")
    OTHER = 0, _("Другое")
    REQUEST = 12, _("Заявка")
    QUARTILE = 5, _("Квартиль")
    SCAN_COPY = 1, _("Ксерокопия")
    MONOGRAPH = 3, _("Монография")
    SCREEN = 2, _("Скриншот")
    PATENT = 7, _("Патент")
    ORDER = 11, _("Приказ")
    PERCENTILE = 6, _("Процентиль")
    PUBLICATION = 4, _("Публикация")
    DISPOSITION = (
        10,
        _("Распоряжение"),
    )
    EVIDENCE = 8, _("Свидетельство")
    ACCREDITATION_CERTIFICATE = 17, _("Свидетельство об аккредитации")
    CERTIFICATE = 19, _("Сертификат")
    OFFICIAL_NOTE_OF_THE_CHAIRMAN = (
        14,
        _("Служебная записка"),
    )
    REFERENCE = 9, _("Справка")
    INTRODUCTION_HELP = 15, _("Справка о внедрении")
    CERTIFICATION = 21, _("Удостоверение")


TYPE_CATEGORY = get_choices(TypeCategory)
TYPE_FILE = get_choices(TypeFile)
COLLABORATORS = get_choices(Collaborators)
STATUS_QUESTIONARY = get_choices(StatusQuestionnaire)
