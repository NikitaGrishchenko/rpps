def total_score_of_all_users(data):
    """ Общий балл"""

    sum_points = 0

    for faculty in data:
        sum_points += faculty["points"]

    return round(sum_points, 2)
