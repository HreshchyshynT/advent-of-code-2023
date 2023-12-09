from util import get_input

move_to_index = {'L': 0, 'R': 1}


def part_2(input: list[str]):
    print("part 2: ")


def part_1(input: list[str]):
    moves = input[0]
    nodes = {}

    for i in range(2, len(input)):
        node = input[i].split(" = ")[0]
        paths = input[i].split(" = ")[1][1:-1].split(", ")
        nodes[node] = paths

    current_node = input[2].split(" = ")[0]
    count = 0
    i = 0
    while current_node != 'ZZZ':
        move = moves[i % len(moves)]
        print(f"i {i} count {count} node {current_node} move {move}")
        current_node = nodes[current_node][move_to_index[move]]
        count += 1
        i += 1
    print(f"part 1: {count}")


def run():
    input = get_input(8)
    part_1(input.splitlines())
    part_2(test_input.splitlines())


test_input = """
LLR

AAA = (BBB, BBB)
BBB = (AAA, ZZZ)
ZZZ = (ZZZ, ZZZ)
""".strip()
