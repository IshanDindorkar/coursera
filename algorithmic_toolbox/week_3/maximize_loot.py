# Created by Ishan Dindorkar on 18/09/22
# Email: Ishan.Dindorkar@yahoo.com
"""
Implementation of knapsack algorithm calculate maximum loot value
"""
from typing import List


def main(capacity: int, cost_weight_list: List):
    value = maximize_loot(capacity=capacity, cost_weight_list=cost_weight_list)
    print("{:.10f}".format(value))


def maximize_loot(capacity: int, cost_weight_list: List):
    cost_weight_list.sort(key=lambda x: (x[0] / x[1]), reverse=True)  # sort the array in the decreasing order of cost is to weight ratio
    value = 0
    for (cost, weight) in cost_weight_list:
        if capacity == 0:
            break
        if weight <= capacity:
            value += cost
            capacity -= weight
        else:
            value += float(capacity / weight) * cost
            break

    return value


if __name__ == "__main__":
    num_compounds, capacity = map(int, input().split())
    assert 1 <= num_compounds <= 1000
    assert 0 <= capacity <= 2*10**6

    cost_weight_list = list()
    for idx in range(num_compounds):
        cost, weight = map(int, input().split())
        assert 0 <= cost <= 2 * 10 ** 6
        assert 0 <= weight <= 2 * 10 ** 6
        cost_weight_list.append((cost, weight))

    main(capacity=capacity, cost_weight_list=cost_weight_list)
