from .count_of_teachers import count_of_teachers
from .overall_points_by_main_category import overall_points_by_main_category
from .total_average_score import total_average_score


def average_by_main_category(data):
    """ Средний балл по главным категориям """

    points_by_main_category = overall_points_by_main_category(data)
    count_teachers = count_of_teachers(data)

    result = []

    for key, value in points_by_main_category.items():
        result.append(
            {"name": key, "points": round(value / count_teachers, 2),}
        )
    result.append({"name": "Все разделы", "points": total_average_score(data)})

    return result
