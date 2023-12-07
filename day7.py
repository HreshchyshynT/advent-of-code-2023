from functools import cmp_to_key

from util import get_input

card_map = {
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    'T': 10,
    'J': 11,
    'Q': 12,
    'K': 13,
    'A': 14,
}

card_map_2 = {
    'J': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    'T': 10,
    'Q': 12,
    'K': 13,
    'A': 14,
}


def get_points(hand: str) -> int:
    # Five of a kind - 7
    # Four of a kind - 6
    # Full house - 5
    # Three of a kind - 4
    # Two pair - 3
    # One pair - 2
    # High card - 1
    combination: dict[str, int] = {}
    for c in hand:
        if c not in combination:
            combination[c] = hand.count(c)
    if 5 in combination.values():
        return 7
    elif 4 in combination.values():
        return 6
    elif 3 in combination.values() and 2 in combination.values():
        return 5
    elif 3 in combination.values():
        return 4
    elif 2 in combination.values() and len(combination) == 3:
        return 3
    elif 2 in combination.values():
        return 2
    else:
        return 1


def get_points_p2(hand: str) -> int:
    # Five of a kind - 7
    # Four of a kind - 6
    # Full house - 5
    # Three of a kind - 4
    # Two pair - 3
    # One pair - 2
    # High card - 1
    combination: dict[str, int] = {}
    for c in hand:
        if c not in combination:
            combination[c] = hand.count(c)

    if 'J' in combination and combination['J'] < 5:
        j_count = combination['J']
        del combination['J']
        m_v = 0
        m_k = ''
        for k, v in combination.items():
            if v > m_v:
                m_v = v
                m_k = k
        combination[m_k] = m_v + j_count

    if 5 in combination.values():
        return 7
    elif 4 in combination.values():
        return 6
    elif 3 in combination.values() and 2 in combination.values():
        return 5
    elif 3 in combination.values():
        return 4
    elif 2 in combination.values() and len(combination) == 3:
        return 3
    elif 2 in combination.values():
        return 2
    else:
        return 1


def compare_hands(left: str, right: str) -> int:
    for i in range(len(left)):
        r = card_map[left[i]] - card_map[right[i]]
        if r != 0:
            return r
    return 0


def compare_hands_p2(left: str, right: str) -> int:
    for i in range(len(left)):
        r = card_map_2[left[i]] - card_map_2[right[i]]
        if r != 0:
            return r
    return 0


def part_1(input: list[str]):
    hands_and_bids = {}
    for i in input:
        s = i.split(" ")
        hands_and_bids[s[0]] = int(s[1])
    hands_and_points = [[] for _ in range(8)]
    for (hand, _) in hands_and_bids.items():
        points = get_points(hand)
        hands_and_points[points].append(hand)
        hands_and_points[points] = sorted(hands_and_points[points], key=cmp_to_key(compare_hands))

    result = 0
    rank = 0
    for hands in hands_and_points:
        for hand in hands:
            rank += 1
            result += (rank * hands_and_bids[hand])

    print(f"part 1: {result}")


def part_2(input: list[str]):
    hands_and_bids = {}
    for i in input:
        s = i.split(" ")
        hands_and_bids[s[0]] = int(s[1])
    hands_and_points = [[] for _ in range(8)]
    for (hand, _) in hands_and_bids.items():
        points = get_points_p2(hand)
        hands_and_points[points].append(hand)
        hands_and_points[points] = sorted(hands_and_points[points], key=cmp_to_key(compare_hands_p2))

    result = 0
    rank = 0
    print(hands_and_points)
    for hands in hands_and_points:
        for hand in hands:
            rank += 1
            result += (rank * hands_and_bids[hand])

    print(f"part 2: {result}")


def run():
    input = get_input(7)
    part_1(input.splitlines())
    part_2(input.splitlines())


test_input = """
32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483
""".strip()
