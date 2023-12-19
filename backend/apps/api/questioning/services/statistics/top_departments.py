def top_departments(data):
    """ Рейтинг кафедр """

    result = []

    for faculty in data:
        for department in faculty["departments"]:
            result.append(
                {
                    "name": department["name"],
                    "points": round(
                        department["points"] / department["count_users"], 2
                    ),
                }
            )
    result = reversed(
        sorted(result, key=lambda department: department["points"])
    )

    return result
