def grading_students(grades):
    # If the difference between the grade
    #   and the next multiple of 5 is less than 3,
    #   round grade up to the next multiple of 5.

    # If the value of grade is less than 38,
    #   no rounding occurs as the result will still be a failing grade.
    collection = []
    for g in grades:
        diff = 5 - g % 5
        if g < 38:
            adj_grade = g
        elif diff < 3:
            adj_grade = g + diff
        else:
            adj_grade = g
        collection.append(adj_grade)

    return collection
