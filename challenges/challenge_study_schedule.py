def study_schedule(permanence_period, target_time):
    try:
        students_counter = 0
        for class_starting, class_finished in permanence_period:
            if class_starting <= target_time <= class_finished:
                students_counter += 1
        return students_counter
    except TypeError:
        return None
