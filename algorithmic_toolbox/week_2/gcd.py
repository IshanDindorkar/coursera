# Created by Ishan Dindorkar on 05/09/22
# Email: Ishan.Dindorkar@yahoo.com

"""
Greatest Common Divisor problem using Naive and Euclidean Algorithms
"""
import time

from loguru import logger


def main(num_a: int, num_b: int):
    # GCD calculation using Euclidean algorithm (efficient)
    start_time = time.time()
    logger.info(calculate_gcd_euclidean_algo(num_a=num_a, num_b=num_b))
    end_time = time.time()
    logger.info(f"Time taken for Euclidean algorithm is {end_time - start_time}")

    # GCD calculation using Naive algorithm (inefficient)
    start_time = time.time()
    logger.info(calculate_gcd_naive_algo(num_a=num_a, num_b=num_b))
    end_time = time.time()
    logger.info(f"Time taken for Naive algorithm is {end_time - start_time}")


def calculate_gcd_naive_algo(num_a: int, num_b: int):
    gcd = 0
    for x in range(1, num_a + num_b):
        if (num_a % x == 0) and (num_b % x == 0):
            gcd = x

    return gcd


def calculate_gcd_euclidean_algo(num_a: int, num_b: int):
    if num_b == 0:
        return num_a

    a_prime = num_a % num_b  #
    return calculate_gcd_euclidean_algo(num_b, a_prime)


if __name__ == "__main__":
    num_a, num_b = map(int, input().split())
    main(num_a=num_a, num_b=num_b)


"""
Discussion: 

Lemma =>
gcd(a, b) = gcd(a_prime, b) = gcd(b, a_prime)
a = a_prime + bq for some q
d(divisor) divides a and b if and only if it divides a_prime and b 

Algorithm =>
function euclidGCD(a, b):
    if b = 0:
        return a
    a_prime <- the remainder when a is divided by b
    
    return euclidGCD(b, a_prime)
    
Time complexity =>
O(n) = log(ab)
"""