# Created by Ishan Dindorkar on 10/09/22
# Email: Ishan.Dindorkar@yahoo.com

"""
Course Week 2 Programming Assignment:
Part 2/8 => Find last digit of a large Fibonacci number
"""


def main(num_elem: int):
    assert 0 <= num_elem <= 10 ** 6
    print(get_last_digit_fibonacci_number(num_elem=num_elem + 1))


def get_last_digit_fibonacci_number(num_elem: int):
    fibonacci_series = [0, 1]

    for idx in range(2, num_elem):
        sum_last_two_nums = fibonacci_series[idx - 1] + fibonacci_series[idx - 2]
        fibonacci_series.append(sum_last_two_nums % 10)

    return fibonacci_series[num_elem - 1]


if __name__ == "__main__":
    num_elem = int(input())
    main(num_elem=num_elem)
