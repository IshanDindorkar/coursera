# Created by Ishan Dindorkar on 04/09/22
# Email: Ishan.Dindorkar@yahoo.com

"""
Code to get Nth number from Fibonacci series using an efficient algorithm and less
efficient algorithm
"""
import time

from loguru import logger


def main(num_elem: int):
    start_time = time.time()
    result = get_element_from_fibonacci_series_eff_algo(num_elem=num_elem)
    end_time = time.time()
    logger.info(f"Result: {result}")
    logger.info(f"Time taken for an efficient version of algorithm: {end_time - start_time}")

    start_time = time.time()
    result = get_element_from_fibonacci_series_ineff_algo(num_elem=num_elem - 1)
    end_time = time.time()
    logger.info(f"Result: {result}")
    logger.info(f"Time taken for an inefficient version of algorithm: {end_time - start_time}")


def get_element_from_fibonacci_series_eff_algo(num_elem: int):
    fibonacci_series = [0, 1]

    for idx in range(2, num_elem):
        fibonacci_series.append(fibonacci_series[idx - 1] + fibonacci_series[idx - 2])

    return fibonacci_series[num_elem - 1]


def get_element_from_fibonacci_series_ineff_algo(num_elem: int):
    if num_elem <= 1:
        return num_elem
    return get_element_from_fibonacci_series_ineff_algo(num_elem=num_elem - 1) + \
           get_element_from_fibonacci_series_ineff_algo(num_elem=num_elem - 2)


if __name__ == "__main__":
    num_elem = int(input())
    main(num_elem=num_elem)
