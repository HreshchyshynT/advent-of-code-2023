from util import get_input


def part_2(input: list[str]):
    print("part 2: ")


def arrange_row(springs: str, groups: list[int]) -> (int, bool):
    if len(groups) == 0:
        return 1, all([c != '#' for c in springs])
    group = groups[0]
    count = 0
    for i in range(len(springs) - sum(groups) + 1):
        if springs[i] not in {'#', '?'}:
            continue
        can_arrange = all([c != '.' for c in springs[i: i + group]])
        left_ok = all(c != '#' for c in springs[:i])
        right_ok = i + group == len(springs) or springs[i + group] == '.' or springs[i + group] == '?'
        if not can_arrange or not left_ok or not right_ok:
            continue
        next_arrangement = arrange_row(springs[i + group + 1:], groups[1:])
        if next_arrangement[1]:
            count += next_arrangement[0]
    return count, count != 0


def part_1(input: list[str]):
    arrangements = []
    for line in input:
        groups = [int(i) for i in line.split(' ')[1].split(',')]
        springs = line.split(' ')[0]
        arrangements.append((line, arrange_row(springs, groups)[0]))

    print(f"part 1: {sum([a for _, a in arrangements])}")


def run():
    input = get_input(12)
    part_1(input.splitlines())
    part_2(test_input.splitlines())


test_input = """
.?###. 3
?.?..? 1,1
#??# 1,1
?#...???. 1
?#. 1
""".strip()
test_input_2 = """
#..#.??#??#..?? 1,1,1,1
#?..?#?. 1,1
#.?#.#.?#..? 1,1,1,1
#???#.#.#..#.#?## 1,1,1,1,1,1,2
#?#?##?? 1,1,2
""".strip()
test_input_1 = """
???.### 1,1,3
.??..??...?##. 1,1,3
?#?#?#?#?#?#?#? 1,3,1,6
????.#...#... 4,1,1
????.######..#####. 1,6,5
?###???????? 3,2,1
""".strip()
