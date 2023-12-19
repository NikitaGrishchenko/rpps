from contextlib import redirect_stdout


def count_of_teachers(data):
    """ Количество преподавателей у которых points > 0"""

    # пользователей всего
    count_users_all = 0
    # пользователей у которых points > 0
    count_user_action = 0

    plus = 0
    minus = 0

    for faculty in data:
        for department in faculty["departments"]:
            for user in department["users"]:
                if user["points"] > 319:
                    plus += 1
                elif user["points"] < 319 and user["points"] != 0:
                    minus += 1
                count_users_all += 1
                if user["points"] > 0:
                    count_user_action += 1

    # print(plus)
    # print(minus)
    return count_user_action
