def breaking_records(scores):
    most_points = scores[0]
    least_points = most_points
    scores.pop(0)
    counts = [0, 0]
    for s in scores:
        if s > most_points:
            most_points = s
            counts[0] += 1

        if s < least_points:
            least_points = s
            counts[1] += 1

    return counts
