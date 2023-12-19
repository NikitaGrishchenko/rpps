def average_score_for_sections_in_each_faculty(data):
    """ Средний балл по разделам в каждом факультете """
    results = []

    for faculty in data:
        for department in faculty["departments"]:
            for user in department["users"]:
                for ques in user["questionnaire"]:
                    results.append(
                        {"name": ques["name"], "faculties": [],}
                    )
                break
            break
        break
    for result in results:
        for faculty in data:
            points = 0
            count_users = 0
            for department in faculty["departments"]:
                for user in department["users"]:
                    count_users += 1
                    for ques in user["questionnaire"]:
                        if result["name"] == ques["name"]:
                            points += ques["points"]
            result["faculties"].append(
                {
                    "name": faculty["name"],
                    "points": round(points / count_users, 2),
                }
            )

    return results
