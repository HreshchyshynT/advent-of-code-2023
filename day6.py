from util import get_input


def read_numbers(line: str) -> list[int]:
    result = []
    buffer = ""
    for c in line:
        if c.isdigit():
            buffer = buffer + c
        elif len(buffer) != 0:
            result.append(int(buffer))
            buffer = ""

    if len(buffer) != 0:
        result.append(int(buffer))
    return result


def min_charging_time(time: int, distance: int) -> int:
    left = 0
    right = time
    while right - left > 1:
        speed = int((left + right) / 2)
        time_left = time - speed
        if time_left * speed > distance:
            right = speed
        else:
            left = speed
    return right


def max_charging_time(time: int, distance: int) -> int:
    left = 0
    right = time
    while right - left > 1:
        speed = int((left + right) / 2)
        time_left = time - speed
        if time_left * speed > distance:
            left = speed
        else:
            right = speed
    return left


def part_1(input: list[str]):
    time_arr = read_numbers(input[0])
    distances = read_numbers(input[1])

    result = 1

    for i in range(len(time_arr)):
        time = time_arr[i]
        distance = distances[i]
        left = min_charging_time(time, distance)
        right = max_charging_time(time, distance)
        result *= (right - left + 1)

    print(f"part 1: {result}")


def part_2(input: list[str]):
    time = int("".join(filter(str.isdigit, input[0])))
    distance = int("".join(filter(str.isdigit, input[1])))
    result = 1

    left = min_charging_time(time, distance)
    right = max_charging_time(time, distance)
    result *= (right - left + 1)

    print(f"part 2: {result}")


def run():
    input = get_input(6).splitlines()
    part_1(input)
    part_2(input)


test_input = """
Time:      7  15   30
Distance:  9  40  200
""".strip()
