from util import get_input


def parse_numbers(line: str) -> list[int]:
    result = []
    for number in line.strip().split(" "):
        if number != "":
            result.append(int(number.strip()))
    return result


def part_2(input: list[str]):
    cards_count: list[int] = [1] * len(input)
    for i, line in enumerate(input):
        (winning, my) = list(map(parse_numbers, line.split(":")[1].split("|")))
        shift = 0
        for number in my:
            if number in winning:
                shift += 1
                cards_count[i + shift] = cards_count[i + shift] + 1 * cards_count[i]
    print(f"part 2: {sum(cards_count)}")


def part_1(input: list[str]):
    total = 0
    for line in input:
        (winning, my) = list(map(parse_numbers, line.split(":")[1].split("|")))
        points = 0
        for number in my:
            if number in winning:
                if points == 0:
                    points += 1
                else:
                    points *= 2
        total += points
    print(f"part 1: {total}")


def run():
    input = get_input(4)
    part_1(input.splitlines())
    part_2(input.splitlines())


test_input = """
Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11
""".strip()
