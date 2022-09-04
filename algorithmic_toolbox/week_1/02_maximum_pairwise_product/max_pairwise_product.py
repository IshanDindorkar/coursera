"""
Maximum pairwise product algorithm
"""
import time


def main(count_of_numbers: int, list_of_numbers: list):
    # start_time = time.time()
    # max_product = naive_algo_max_pairwise_product(count_of_numbers=count_of_numbers, list_of_numbers=list_of_numbers)
    # end_time = time.time()
    # print(f"Time taken for naive algorithm: {end_time - start_time}")
    # print(f"{max_product}")

    # start_time = time.time()
    max_product = fast_algo_max_pairwise_product(count_of_numbers=count_of_numbers, list_of_numbers=list_of_numbers)
    # end_time = time.time()
    # print(f"Time taken for fast algorithm: {end_time - start_time}")
    print(f"{max_product}")


def naive_algo_max_pairwise_product(count_of_numbers: int, list_of_numbers: list):
    out_index = 0
    max_product = 0
    for oi in range(count_of_numbers):
        out_index += 1

        in_index = 0
        for ii in range(oi + 1, count_of_numbers):
            in_index += 1
            temp_product = list_of_numbers[oi] * list_of_numbers[ii]
            if temp_product > max_product:
                max_product = temp_product

    return max_product


def fast_algo_max_pairwise_product(count_of_numbers: int, list_of_numbers: list):
    largest_number = 0
    largest_number_index = 0

    # first scan of number list to get largest number
    for index in range(count_of_numbers):
        if list_of_numbers[index] > largest_number:
            largest_number = list_of_numbers[index]
            largest_number_index = index

    second_largest_number = 0
    second_largest_index = 0

    # second scan of number list to get second largest number
    for index in range(count_of_numbers):
        if list_of_numbers[index] > second_largest_number and index != largest_number_index:
            second_largest_number = list_of_numbers[index]
            second_largest_index = index

    max_product = largest_number * second_largest_number

    return max_product


if __name__ == "__main__":
    # take input from console
    # 1. total count of numbers
    count_of_numbers = int(input())
    # 2. list of numbers
    list_of_numbers = list(map(int, input().split()))

    main(count_of_numbers=count_of_numbers, list_of_numbers=list_of_numbers)
