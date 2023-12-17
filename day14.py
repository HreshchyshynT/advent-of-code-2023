from util import get_input


def north(i: int, j: int) -> (int, int):
    return i - 1, j


def west(i: int, j: int) -> (int, int):
    return i, j - 1


def south(i: int, j: int) -> (int, int):
    return i + 1, j


def east(i: int, j: int) -> (int, int):
    return i, j + 1


def tilt_item(platform: list[list[str]], i: int, j: int, move):
    current_i = i
    current_j = j

    next_i, next_j = move(i, j)
    while next_i in range(len(platform)) and next_j in range(len(platform[0])):
        current_c = platform[current_i][current_j]
        next_c = platform[next_i][next_j]
        if next_c == '.':
            platform[current_i][current_j] = next_c
            platform[next_i][next_j] = current_c
        else:
            break

        current_i, current_j = next_i, next_j
        next_i, next_j = move(next_i, next_j)


def total_load(platform: list[list[str]]) -> int:
    result = 0
    for i in range(len(platform)):
        for j in range(len(platform[i])):
            if platform[i][j] == 'O':
                result += len(platform) - i
    return result


def tilt_platform_north(platform: list[list[str]]):
    for i in range(len(platform)):
        line = platform[i]
        for j in range(len(line)):
            if platform[i][j] == 'O':
                tilt_item(platform, i, j, north)


def tilt_platform_west(platform: list[list[str]]):
    for i in range(len(platform)):
        line = platform[i]
        for j in range(len(line)):
            if platform[i][j] == 'O':
                tilt_item(platform, i, j, west)


def tilt_platform_south(platform: list[list[str]]):
    for i in reversed(range(len(platform))):
        line = platform[i]
        for j in range(len(line)):
            if platform[i][j] == 'O':
                tilt_item(platform, i, j, south)


def tilt_platform_east(platform: list[list[str]]):
    for i in range(len(platform)):
        line = platform[i]
        for j in reversed(range(len(line))):
            if platform[i][j] == 'O':
                tilt_item(platform, i, j, east)


def to_key(platform: list[list[str]]) -> str:
    str_platform = "".join(["".join(arr) for arr in platform])
    return str_platform


def copy_platform(platform: list[list[str]]) -> list[list[str]]:
    return [line.copy() for line in platform]


def find_key_by_value(d, f):
    for key in d:
        if f(d[key]):
            return key
    return None


def part_2(input: list[str]):
    cycles = 1_000_000_000
    platform = [list(line) for line in input]
    cycle_cache = {}
    i = 0
    while i < cycles:
        key = to_key(platform)
        if key in cycle_cache:
            from_cache = cycle_cache[key]
            cached_i = from_cache[1]
            cycles_to_return = len(cycle_cache) - cached_i
            left_after_repeats = (cycles - i) % cycles_to_return
            last_hit = cached_i + left_after_repeats - 1
            new_key = find_key_by_value(cycle_cache, lambda v: v[1] == last_hit)
            platform = cycle_cache[new_key][0]
            break
        else:
            tilt_platform_north(platform)
            tilt_platform_west(platform)
            tilt_platform_south(platform)
            tilt_platform_east(platform)
            cycle_cache[key] = (copy_platform(platform), i)
        i += 1
    print(f"part 2: {total_load(platform)}")


def part_1(input: list[str]):
    platform = [list(line) for line in input]
    tilt_platform_north(platform)
    print(f"part 1: {total_load(platform)}")


def run():
    input = get_input(14)
    part_1(input.splitlines())
    part_2(input.splitlines())


test_input = """
O....#....
O.OO#....#
.....##...
OO.#O....O
.O.....O#.
O.#..O.#.#
..O..#O..O
.......O..
#....###..
#OO..#....
""".strip()
