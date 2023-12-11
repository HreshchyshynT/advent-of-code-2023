from util import get_input


def part_1(input: list[str]):
    galaxies = []
    empty_rows = set([i for i, _ in enumerate(range(len(input)))])
    empty_columns = set([i for i, _ in enumerate(range(len(input[0])))])

    for i in range(len(input)):
        line = input[i]
        for j in range(len(line)):
            if line[j] == '#':
                galaxies.append((i, j))
                if i in empty_rows:
                    empty_rows.remove(i)
                if j in empty_columns:
                    empty_columns.remove(j)
    paths = []
    for i in range(len(galaxies)):
        for j in range(i + 1, len(galaxies)):
            first = galaxies[i]
            second = galaxies[j]
            v_path = range(min(first[0], second[0]), max(first[0], second[0]))
            h_path = range(min(first[1], second[1]), max([first[1], second[1]]))
            path_len = len(v_path) + len(h_path)
            for r in empty_rows:
                if r in v_path:
                    path_len += 1
            for c in empty_columns:
                if c in h_path:
                    path_len += 1
            paths.append(path_len)
    print(f"part 1: {sum(paths)}")


def part_2(input: list[str]):
    galaxies = []
    empty_rows = set([i for i, _ in enumerate(range(len(input)))])
    empty_columns = set([i for i, _ in enumerate(range(len(input[0])))])

    for i in range(len(input)):
        line = input[i]
        for j in range(len(line)):
            if line[j] == '#':
                galaxies.append((i, j))
                if i in empty_rows:
                    empty_rows.remove(i)
                if j in empty_columns:
                    empty_columns.remove(j)
    paths = []
    for i in range(len(galaxies)):
        for j in range(i + 1, len(galaxies)):
            first = galaxies[i]
            second = galaxies[j]
            v_path = range(min(first[0], second[0]), max(first[0], second[0]))
            h_path = range(min(first[1], second[1]), max([first[1], second[1]]))
            path_len = len(v_path) + len(h_path)
            for r in empty_rows:
                if r in v_path:
                    path_len += (1000000 - 1)
            for c in empty_columns:
                if c in h_path:
                    path_len += (1000000 - 1)
            paths.append(path_len)
    print(f"part 2: {sum(paths)}")


def run():
    input = get_input(11).splitlines()
    part_1(input)
    part_2(input)


test_input = """
...#......
.......#..
#.........
..........
......#...
.#........
.........#
..........
.......#..
#...#.....
""".strip().splitlines()
