# Created by Ishan Dindorkar on 10/09/22
# Email: Ishan.Dindorkar@yahoo.com

"""
Course Week 2 Programming Assignment:
Part 4/8 => Find LCM of two numbers a, b
"""


def main(num_a: int, num_b: int):
    gcd = find_gcd(num_a=num_a, num_b=num_b)
    lcm = int((num_a * num_b) / gcd)   # lcm = product of numbers / gcd of numbers
    print(lcm)


def find_gcd(num_a: int, num_b: int):
    if num_b == 0:
        return num_a

    a_prime = num_a % num_b
    return find_gcd(num_a=num_b, num_b=a_prime)


if __name__ == "__main__":
    num_a, num_b = map(int, input().split())
    main(num_a=num_a, num_b=num_b)
