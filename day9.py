from util import get_input


def extend_sequence_end(values: list[int]) -> list[int]:
    if all(x == 0 for x in values):
        return values + [0]
    new_values = [0] * (len(values) - 1)
    for i in range(len(values) - 1):
        new_values[i] = values[i + 1] - values[i]
    return values + [values[-1] + extend_sequence_end(new_values)[-1]]


def extend_sequence_start(values: list[int]) -> list[int]:
    if all(x == 0 for x in values):
        return [0] + values
    new_values = [0] * (len(values) - 1)
    for i in range(len(values) - 1):
        new_values[i] = values[i + 1] - values[i]
    return [values[0] - extend_sequence_start(new_values)[0]] + values


def part_1(input: list[str]):
    numbers = []
    for line in input:
        values = [int(c) for c in line.split(" ")]
        numbers.append(extend_sequence_end(values))
    print(f"part 1: {sum([sequence[-1] for sequence in numbers])}")


def part_2(input: list[str]):
    numbers = []
    for line in input:
        values = [int(c) for c in line.split(" ")]
        numbers.append(extend_sequence_start(values))
    print(f"part 2: {sum([sequence[0] for sequence in numbers])}")


def run():
    input = get_input(9).splitlines()
    part_1(input)
    part_2(input)


test_input = """
0 3 6 9 12 15
1 3 6 10 15 21
10 13 16 21 30 45
""".strip()
