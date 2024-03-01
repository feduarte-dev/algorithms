def study_schedule(permanence_period, target_time):
    count = 0
    try:
        for join, left in permanence_period:
            if join <= target_time <= left:
                count += 1
        return count
    except (ValueError, TypeError):
        return None
