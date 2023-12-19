import itertools


def top_teachers_by_university(data, place):
    """ Преподаватели, набравшие наибольшее общее
    количество баллов по университету
    """

    result = []

    for faculty in data:
        for department in faculty["departments"]:
            for user in department["users"]:
                result.append(
                    {
                        "name": user["name"],
                        "points": round(user["points"], 2),
                        "faculty": user["faculty"],
                        "department": user["department"],
                    }
                )

    result = itertools.islice(
        reversed(sorted(result, key=lambda user: user["points"])), place
    )

    return result
