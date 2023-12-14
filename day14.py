import time

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


def part_2(input: list[str]):
    platform = [list(line) for line in input]
    cycles = 1_000_000_000
    tilt_north_cache = {}
    tilt_west_cache = {}
    tilt_south_cache = {}
    tilt_east_cache = {}
    start = time.process_time_ns()
    key = to_key(platform)
    for i in range(cycles):
        if key in tilt_north_cache:
            platform, key = tilt_north_cache.get(key)
        else:
            tilt_platform_north(platform)
            new_key = to_key(platform)
            tilt_north_cache[key] = (platform.copy(), new_key)
            key = new_key

        if key in tilt_west_cache:
            platform, key = tilt_west_cache.get(key)
        else:
            tilt_platform_west(platform)
            new_key = to_key(platform)
            tilt_west_cache[key] = (platform.copy(), new_key)
            key = new_key

        if key in tilt_south_cache:
            platform, key = tilt_south_cache.get(key)
        else:
            tilt_platform_south(platform)
            new_key = to_key(platform)
            tilt_south_cache[key] = (platform.copy(), new_key)
            key = new_key

        if key in tilt_east_cache:
            platform, key = tilt_east_cache.get(key)
        else:
            tilt_platform_east(platform)
            new_key = to_key(platform)
            tilt_east_cache[key] = (platform.copy(), new_key)
            key = new_key
        # print(f"i = {i}, h {hits} m {miss}")
    print(f"ends in  {time.process_time_ns() - start}")
    result = total_load(platform)
    print(f"part 2: {result}")


def part_1(input: list[str]):
    platform = [list(line) for line in input]
    result = 0
    tilt_platform_north(platform)
    for i in range(len(platform)):
        for j in range(len(platform[i])):
            if platform[i][j] == 'O':
                result += len(platform) - i
    print(f"part 1: {result}")


def run():
    input = get_input(14)
    part_1(test_input.splitlines())
    part_2(test_input.splitlines())


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
