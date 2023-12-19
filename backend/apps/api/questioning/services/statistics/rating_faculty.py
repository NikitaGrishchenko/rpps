def rating_faculty(data):
    """ Рейтинг по факультету """

    result = []
    for faculty in data:
        result.append(
            {
                "name": faculty["name"],
                "points": round(faculty["points"] / faculty["count_users"], 2),
            }
        )
    return result
