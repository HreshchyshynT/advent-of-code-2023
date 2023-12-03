from util import get_input


def is_symbol(c: str) -> bool:
    return not c.isdigit() and c != "."


def has_adjacent_symbol(input: list[str], i: int, j: int) -> bool:
    adjacent_indexes = [
        (i - 1, j),  # left
        (i - 1, j - 1),  # top left
        (i, j - 1),  # top
        (i + 1, j - 1),  # top right
        (i + 1, j),  # right
        (i + 1, j + 1),  # right bot
        (i, j + 1),  # bot
        (i - 1, j + 1),  # left bot
    ]
    y_range = range(len(input))
    # suppose all lines have the same length
    x_range = range(len(input[0]))
    for (x, y) in adjacent_indexes:
        if x in x_range and y in y_range and is_symbol(input[x][y]):
            return True
    return False


def part_1(input: list[str]):
    total = 0
    for i in range(len(input)):
        line = input[i]
        buffer = ""
        is_part_number = False
        for j in range(len(line)):
            c = line[j]
            if c.isdigit():
                buffer += c
                if has_adjacent_symbol(input, i, j):
                    is_part_number = True
            if not c.isdigit() or j + 1 == len(line):
                if len(buffer) > 0 and is_part_number:
                    total += int(buffer)
                buffer = ""
                is_part_number = False

    print(f"part 1: {total}")


def get_adjacent_numbers(input: list[str], i: int, j: int) -> list[int]:
    adjacent_indexes = [
        (i - 1, j),  # left
        (i - 1, j - 1),  # top left
        (i, j - 1),  # top
        (i + 1, j - 1),  # top right
        (i + 1, j),  # right
        (i + 1, j + 1),  # right bot
        (i, j + 1),  # bot
        (i - 1, j + 1),  # left bot
    ]
    y_range = range(len(input))
    # suppose all lines have the same length
    x_range = range(len(input[0]))

    used_indexes = set()

    result = []

    for (x, y) in adjacent_indexes:
        if (x, y) not in used_indexes and x in x_range and y in y_range and input[x][y].isdigit():
            buffer = ""
            start = x
            line = input[x]
            for i in range(y, -1, -1):
                if line[i].isdigit():
                    start = i
                else:
                    break
            for i in range(start, len(line)):
                used_indexes.add((x, i))
                c = line[i]
                if c.isdigit():
                    buffer += c
                else:
                    break
            result.append(int(buffer))

    return result


def part_2(input: list[str]):
    total = 0
    for i in range(len(input)):
        line = input[i]
        for j in range(len(line)):
            c = line[j]
            if c == '*':
                numbers = get_adjacent_numbers(input, i, j)
                if len(numbers) == 2:
                    total += (numbers[0] * numbers[1])
    print(f"part 2: {total}")


def run():
    input = get_input(3).splitlines()
    # input = test_input.splitlines()
    part_1(input)
    part_2(input)


test_input = """
467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..
""".strip()
