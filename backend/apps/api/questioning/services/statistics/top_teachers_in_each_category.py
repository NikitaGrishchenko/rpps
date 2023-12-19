import itertools


def top_teachers_in_each_category(data, place):
    """ Топ преподавателей в каждой категории (средний балл) """
    results = []

    for faculty in data:
        for department in faculty["departments"]:
            for user in department["users"]:
                for ques in user["questionnaire"]:
                    results.append(
                        {"name": ques["name"], "users": [],}
                    )
                break
            break
        break

    for result in results:
        for faculty in data:
            for department in faculty["departments"]:
                for user in department["users"]:
                    for ques in user["questionnaire"]:
                        if result["name"] == ques["name"]:
                            result["users"].append(
                                {
                                    "name": user["name"],
                                    "faculty": user["faculty"],
                                    "department": user["department"],
                                    "points": round(ques["points"], 2),
                                }
                            )

    for result in results:
        result["users"] = itertools.islice(
            reversed(sorted(result["users"], key=lambda fac: fac["points"])),
            place,
        )

    return results
