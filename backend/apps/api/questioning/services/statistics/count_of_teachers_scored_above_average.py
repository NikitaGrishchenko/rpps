from .average_by_main_category import average_by_main_category


def count_of_teachers_scored_above_average(data):
    """ Количество преподавателей, набравших баллы выше среднего """
    result = []
    average = average_by_main_category(data)

    for a in average:
        result.append(
            {"name": a["name"], "count_users": 0, "points": a["points"]}
        )
    for faculty in data:
        for department in faculty["departments"]:
            for user in department["users"]:
                for ques in user["questionnaire"]:
                    for a in result:
                        if ques["name"] == a["name"]:
                            if ques["points"] > a["points"]:
                                a["count_users"] += 1
                        if a["name"] == "Все разделы":
                            if (
                                user["points"] > a["points"]
                                and user["points"] > 0
                            ):
                                a["count_users"] += 1 / 4

    return result
