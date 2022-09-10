# Created by Ishan Dindorkar on 10/09/22
# Email: Ishan.Dindorkar@yahoo.com

"""
Course Week 2 Programming Assignment:
Part 2/8 => Find n th Fibonacci number mod m
Hint: Use Pisano period algorithm: https://stackoverflow.com/a/64061448
"""


def main(num_elem: int, mod: int):
    assert 1 <= num_elem <= 10 ** 14
    assert 2 <= mod <= 10 ** 3
    print(get_huge_fibonacci_number(num_elem=num_elem + 1, mod=mod))


def get_pisano_period(mod: int):
    prev, curr = 0, 1
    for idx in range(0, mod * mod):
        prev, curr = curr, (curr + prev) % mod
        if prev == 0 and curr == 1:
            return idx + 1


def get_huge_fibonacci_number(num_elem: int, mod: int):
    pisano_period = get_pisano_period(mod=mod)
    num_elem = num_elem % pisano_period
    fibonacci_series = [0, 1]

    for idx in range(2, num_elem):
        sum_last_two_nums = fibonacci_series[idx - 1] + fibonacci_series[idx - 2]
        fibonacci_series.append(sum_last_two_nums)

    return fibonacci_series[num_elem - 1] % mod


if __name__ == "__main__":
    num_elem, mod = map(int, input().split())
    main(num_elem=num_elem, mod=mod)
