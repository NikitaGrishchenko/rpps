def overall_points_by_main_category(data):
    """ общий балл по главным категориям """

    result = {}
    for faculty in data:
        for department in faculty["departments"]:
            for user in department["users"]:
                for main_category_user in user["questionnaire"]:
                    if main_category_user["name"] in result.keys():
                        result[
                            main_category_user["name"]
                        ] += main_category_user["points"]
                    else:
                        result[
                            main_category_user["name"]
                        ] = main_category_user["points"]
    return result
