# Created by Ishan Dindorkar on 18/09/22
# Email: Ishan.Dindorkar@yahoo.com

"""
Algorithmic implementation to calculate maximum advertisement revenue
"""
from typing import List
import numpy as np


def main(num_of_ad_slots: int,
         price_per_click: List,
         num_of_clicks_per_slot: List):
    print(max_ad_revenue(num_of_ad_slots=num_of_ad_slots,
                         price_per_click=price_per_click,
                         num_of_clicks_per_slot=num_of_clicks_per_slot))

    # print(max_ad_revenue_dot_prod(price_per_click=price_per_click,
    #                               num_of_clicks_per_slot=num_of_clicks_per_slot))


def max_ad_revenue(num_of_ad_slots: int,
                   price_per_click: List,
                   num_of_clicks_per_slot: List):
    assert num_of_ad_slots == len(price_per_click) == len(num_of_clicks_per_slot)

    total_revenue = 0
    for idx in range(num_of_ad_slots):
        total_revenue += price_per_click[idx] * num_of_clicks_per_slot[idx]  # dot product

    return total_revenue


def max_ad_revenue_dot_prod(price_per_click: List,
                            num_of_clicks_per_slot: List):
    return np.dot(price_per_click, num_of_clicks_per_slot)


if __name__ == "__main__":
    # inputs
    num_of_ad_slots = int(input())
    price_per_click = list(map(int, input().split()))
    num_of_clicks_per_slot = list(map(int, input().split()))

    # validations
    assert 1 <= num_of_ad_slots <= 10 ** 3
    for price in sorted(price_per_click):
        assert 0 <= price
    for clicks in sorted(num_of_clicks_per_slot):
        assert 0 <= clicks

    main(num_of_ad_slots=num_of_ad_slots,
         price_per_click=sorted(price_per_click, reverse=True),
         num_of_clicks_per_slot=sorted(num_of_clicks_per_slot, reverse=True))
