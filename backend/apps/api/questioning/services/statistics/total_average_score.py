from .count_of_teachers import count_of_teachers
from .total_score_of_all_users import total_score_of_all_users


def total_average_score(data):
    """ Общий средний балл """

    result = total_score_of_all_users(data) / count_of_teachers(data)
    return round(result, 2)
