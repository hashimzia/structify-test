def count_intersections(radian_measures, identifiers):
    chord_events = []
    intersection_count = 0

    for i in range(len(identifiers)):
        if identifiers[i][0] == 's':
            chord_events.append((radian_measures[i], 1))  # Start of chord
        else:
            chord_events.append((radian_measures[i], -1))  # End of chord

    chord_events.sort()

    active_chords = 0
    for event in chord_events:
        active_chords += event[1]
        if event[1] == 1:  # If it's the start of a chord
            intersection_count += active_chords - 1

    return intersection_count

# Example usage
radians = [0.78, 1.47, 1.77, 3.92]
identifiers = ["s1", "s2", "e1", "e2"]
result_1 = count_intersections(radians,identifiers)
print(result_1 ,"intersection(s)")
