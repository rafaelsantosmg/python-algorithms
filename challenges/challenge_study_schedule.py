def study_schedule(permanence_period, target_time):
    count = 0
    try:
        for permanence in permanence_period:
            if target_time >= permanence[0] and target_time <= permanence[1]:
                count += 1

    except TypeError:
        return None
    return count
