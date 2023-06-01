def study_schedule(permanence_period, target_time):
    try:
        result = {}
        for period in permanence_period:
            hour = period[0]
            while hour <= period[1]:
                result[hour] = result.get(hour, 0) + 1
                hour += 1

        return result[target_time]
    except Exception:
        return None
