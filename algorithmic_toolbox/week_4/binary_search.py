# Created by Ishan Dindorkar on 29/09/22
# Email: Ishan.Dindorkar@yahoo.com


"""
Implement Binary Search algorithm
"""
from typing import List


def main(elements: List, key: int):
    # sort the array of given elements
    sorted_elements = sorted(elements)  # mandatory to have array sorted for binary search algorithm to work
    print(f"Sorted array of elements: {sorted_elements}")

    low = 0
    high = len(elements)
    index = binary_search(elements=sorted_elements, low=low, high=high, key=key) + 1

    print(f"Key is either found or inserted at the following position in array: {index}")


def binary_search(elements: List, low: int, high: int, key: int) -> int:
    # define base condition
    if high <= low:
        return low - 1  # all elements in the array are greater than given key

    # define exit condition
    mid_index = int(low + ((high - low) / 2))
    if key == elements[mid_index]:
        return mid_index
    elif key <= elements[mid_index]:  # search in lower half of array
        return binary_search(elements=elements, low=low, high=mid_index - 1, key=key)
    else:  # search in upper half of array
        return binary_search(elements=elements, low=mid_index + 1, high=high, key=key)


if __name__ == "__main__":
    elements = list(map(int, input().split()))
    key = int(input())

    main(elements, key)
