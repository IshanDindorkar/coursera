# Created by Ishan Dindorkar on 14/09/22
# Email: Ishan.Dindorkar@yahoo.com
"""
Design greedy algorithm to maximize the loot value
"""
from typing import List


def main(capacity: int, compound_weights: List, compound_costs: List):
    print(maximize_loot(capacity=capacity, compound_weights=compound_weights, compound_costs=compound_costs))


def maximize_loot(capacity: int, compound_weights: List, compound_costs: List):
    if capacity == 0 or len(compound_weights) == 0:
        return 0

    # 1. find the most expensive compound
    m = find_most_expensive_compound(compound_costs=compound_costs)

    # 2. find optimum value for "a"
    a = min(compound_weights[m], capacity)

    # 3. maximize value using most expensive compound
    val_most_exp_comp = int((compound_costs[m] * compound_weights[m]) * (a / compound_weights[m]))
    capacity -= compound_weights[m] * (a / compound_weights[m])

    # 4. delete elements corresponding to most expensive compound from weight and cost arrays
    del compound_weights[m]
    del compound_costs[m]

    return val_most_exp_comp + maximize_loot(capacity=capacity, compound_weights=compound_weights,
                                             compound_costs=compound_costs)


def find_most_expensive_compound(compound_costs: List):
    max_value = 0
    idx_most_exp_comp = 0
    for idx, cost in enumerate(compound_costs):
        if cost > max_value:
            max_value = cost
            idx_most_exp_comp = idx

    return idx_most_exp_comp


if __name__ == "__main__":
    capacity = int(input())
    compound_weights = list(map(int, input().split()))
    compound_costs = list(map(int, input().split()))

    main(capacity=capacity, compound_weights=compound_weights, compound_costs=compound_costs)
