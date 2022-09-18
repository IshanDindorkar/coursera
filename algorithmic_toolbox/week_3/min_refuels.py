# Created by Ishan Dindorkar on 15/09/22
# Email: Ishan.Dindorkar@yahoo.com

"""
Greedy algorithm to refuel at the farthest refueling station
"""
from typing import List


def main(car_mileage: int, total_distance: int, stops: List):
    start_location = 0
    assert sorted(stops) == stops  # check for constraint that stop distances should be in increasing order

    num_refills = (refills(current_location=start_location, car_mileage=car_mileage, total_distance=total_distance,
                           stops=stops))
    if num_refills == float("inf"):
        print("-1")
    else:
        print(num_refills)


def refills(current_location: int, car_mileage: int, total_distance: int, stops: List):
    # no need to refuel if car can travel total distance with existing level of fuel tank
    if current_location + car_mileage >= total_distance:
        return 0

    # if distance between current location and first stop is greater than mileage, problem is unsolvable
    if len(stops) == 0 or (stops[0] - current_location) > car_mileage:
        # if len(stops) > 0:
            # print(f"Not enough fuel to reach from current location {current_location} miles to "
            #       f"next fuel station {stops[0]} miles away")
        return float("inf")

    # move car to first refuel station in the list of stops
    last_stop = current_location
    while len(stops) > 0 and (stops[0] - current_location) <= car_mileage:
        last_stop = stops[0]
        # print(f"Car reached fuel station at distance: {stops[0]} miles")
        del stops[0]

    # print(f"Car is refueling at fuel station at distance {last_stop} miles")
    return 1 + refills(current_location=last_stop, car_mileage=car_mileage,
                       total_distance=total_distance, stops=stops)


if __name__ == "__main__":
    total_distance = int(input())
    car_mileage = int(input())
    num_of_stops = int(input())
    stops = list(map(int, input().split()))

    # assertions to check boundary conditions
    assert 1 <= total_distance <= 10**5
    assert 1 <= car_mileage <= 400
    assert 1 <= num_of_stops <= 300
    sorted_stops = sorted(stops)
    assert 0 < sorted_stops[0] < sorted_stops[num_of_stops - 1] < total_distance

    main(car_mileage=car_mileage, total_distance=total_distance, stops=stops)
