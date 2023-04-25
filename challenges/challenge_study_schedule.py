def study_schedule(permanence_period, target_time):
    students_counter = 0

    if not target_time or not permanence_period:
        return None

    for class_starting, class_finished in permanence_period:
        if (type(class_starting) is not int) or type(
            class_finished
        ) is not int:
            return None
        if class_starting <= target_time <= class_finished:
            students_counter += 1

    return students_counter
