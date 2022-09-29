# Created by Ishan Dindorkar on 18/09/22
# Email: Ishan.Dindorkar@yahoo.com

"""
Algorithmic implementation for covering segments by points problem
"""
from typing import List


def main(num_segments: int, segment_coordinates: List):
    # Step 1: sort segment coordinates
    sorted_segment_coordinates = sorted(segment_coordinates, key=lambda k: k[1])  # sort by second element

    # Step 2: Initialize minimum point tracker with the first segment coordinates in the sorted list
    min_point_tracker = [str(sorted_segment_coordinates[0][1])]
    for (l, r) in sorted_segment_coordinates:
        # Keep looping until first element of tuple is less than top point in the tracker
        if l <= int(min_point_tracker[len(min_point_tracker) - 1]):
            continue
        else:
            min_point_tracker.append(str(r))

    print(len(min_point_tracker))
    print(" ".join(min_point_tracker))


if __name__ == "__main__":
    num_segments = int(input())
    assert 1 <= num_segments <= 100

    segment_coordinates = list()
    for idx in range(num_segments):
        segment_coordinate = tuple(map(int, input().split()))
        assert 0 <= segment_coordinate[0] <= segment_coordinate[1] <= 10 ** 9
        segment_coordinates.append(segment_coordinate)

    main(num_segments=num_segments, segment_coordinates=segment_coordinates)
