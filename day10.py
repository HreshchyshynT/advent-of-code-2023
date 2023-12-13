from util import get_input


class Point:
    i: int
    j: int

    def __init__(self, i: int, j: int):
        self.i = i
        self.j = j

    def __str__(self):
        return f"i: {self.i}, j: {self.j}"


def moves_to_s(current: Point, previous: Point, input: list[str]) -> int:
    symbol = input[current.i][current.j]
    count = 0
    while symbol != 'S':
        count += 1
        next = None
        if symbol == '|':
            m = current.i - previous.i
            next = Point(current.i + m, current.j)
        elif symbol == '-':
            m = current.j - previous.j
            next = Point(current.i, current.j + m)
        elif symbol == 'L':
            di = current.j - previous.j
            dj = current.i - previous.i
            next = Point(current.i + di, current.j + dj)
        elif symbol == 'J':
            di = previous.j - current.j
            dj = previous.i - current.i
            next = Point(current.i + di, current.j + dj)
        elif symbol == '7':
            di = current.j - previous.j
            dj = current.i - previous.i
            next = Point(current.i + di, current.j + dj)
        elif symbol == 'F':
            di = previous.j - current.j
            dj = previous.i - current.i
            next = Point(current.i + di, current.j + dj)
        if next:
            previous = current
            current = next
            symbol = input[current.i][current.j]
        else:
            break
    return count


def part_2(input: list[str]):
    print("part 2: ")


def part_1(input: list[str]):
    s_i = 0
    s_j = 0
    for i in range(len(input)):
        for j in range(len(input[i])):
            if input[i][j] == 'S':
                s_i = i
                s_j = j
                break

    moves = moves_to_s(Point(s_i + 1, s_j), Point(s_i, s_j), input) + 1
    print(f"part 1: ({s_i},{s_j}), moves: {moves / 2}")


def run():
    input = get_input(10)
    part_1(input.splitlines())
    part_2(test_input_1.splitlines())


test_input_1 = """
.....
.S-7.
.|.|.
.L-J.
.....
""".strip()

test_input_2 = """
..F7.
.FJ|.
SJ.L7
|F--J
LJ...
""".strip()
