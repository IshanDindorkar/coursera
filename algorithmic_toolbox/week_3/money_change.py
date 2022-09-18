# Created by Ishan Dindorkar on 12/09/22
# Email: Ishan.Dindorkar@yahoo.com

"""
Use Greedy search algorithm to find minimum number of coins that will change given
amount
"""
from typing import List


def main(input_amount: int, denominations=None):
    print(change(input_amount=input_amount, coins=0, denominations=denominations))


def change(input_amount: int, coins: int, denominations=None):
    if denominations is None:
        denominations = [1, 5, 10]

    if input_amount == 0:
        return coins

    if input_amount > 0:
        for denomination in sorted(denominations, reverse=True):
            if denomination <= input_amount:
                input_amount = input_amount - denomination
                coins += 1

                return change(input_amount=input_amount, coins=coins, denominations=denominations)


if __name__ == "__main__":
    input_amount = int(input())
    assert 1 <= input_amount <= 1000

    main(input_amount=input_amount)

