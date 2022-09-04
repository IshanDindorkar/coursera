def main(num_1: int, num_2: int):
    return add_numbers(num_1=num_1, num_2=num_2)


def add_numbers(num_1: int, num_2: int):
    return num_1 + num_2


if __name__ == "__main__":
    num_1, num_2 = map(int, input().split())
    result = main(num_1=num_1, num_2=num_2)
    print(f"{result}")
