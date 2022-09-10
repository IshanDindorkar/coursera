# Created by Ishan Dindorkar on 10/09/22
# Email: Ishan.Dindorkar@yahoo.com

"""
Course Week 2 Programming Assignment:
Part 6/8 => Find last digit of sum of Fibonacci numbers
"""


def main(num_elem: int):
    assert 0 <= num_elem <= 10 ** 14
    print((get_huge_fibonacci_number(num_elem=num_elem + 3, mod=10) - 1) % 10)


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

    return fibonacci_series[num_elem - 1]


if __name__ == "__main__":
    num_elem = int(input())
    main(num_elem=num_elem)


"""
Discussion:
S(n) = F0 + F1 + F2 + F3 ....... Fn
S(n) = F(n+2) – 1
where 
S(n) = sum of "n" Fibonacci numbers
F(n+2) = "n+2" th Fibonacci number
 
"""