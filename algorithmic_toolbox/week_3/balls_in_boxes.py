# Created by Ishan Dindorkar on 18/09/22
# Email: Ishan.Dindorkar@yahoo.com

"""
Algorithm for right combination of balls in boxes problem
"""
import random


def main(total_balls: int, total_boxes: int):
    num_seen_before = set()
    final_sequence = list()
    remaining_balls = total_balls

    for idx in range(1, total_boxes):
        if remaining_balls > 0:
            num_of_ball_in_box = random.randrange(0, remaining_balls)
            if num_of_ball_in_box not in num_seen_before:
                num_seen_before.add(num_of_ball_in_box)
                final_sequence.append(num_of_ball_in_box)
                remaining_balls = total_balls - sum(final_sequence)
        else:
            final_sequence.append(remaining_balls)

    if total_balls - sum(final_sequence) > 0:
        final_sequence.append(total_balls - sum(final_sequence))
    print(f"Sequence of balls: {final_sequence}")


if __name__ == "__main__":
    total_balls = int(input("Enter number of balls: "))
    total_boxes = int(input("Enter number of boxes: "))

    main(total_balls=total_balls, total_boxes=total_boxes)


