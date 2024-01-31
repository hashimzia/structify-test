# Chord Intersection Counter

## Algorithm Explanation

The algorithm combines the start and end points of chords with their identifiers, sorts them based on radian measure, and iterates through the sorted list to count intersections. The intersections are counted by keeping track of active chords.

## How to Run

1. Ensure you have Python installed.
2. Download the provided Python script (`chord_intersection_counter.py`).
3. Modify the `radians` and `intersections` lists as needed.
4. Run the script.

```bash
python chord_intersections.py
```

## Big-O Runtime Estimation
The sorting step dominates the runtime, resulting in O(n log n) complexity, where n is the number of chords.
