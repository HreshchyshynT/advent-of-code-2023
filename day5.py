from util import get_input


def part_2(input: list[str]):
    seeds_ranges = []
    seeds = [int(x) for x in input[0].split(":")[1].strip().split(" ")]
    for i in range(0, len(seeds), 2):
        seeds_ranges.append(range(seeds[i], seeds[i] + seeds[i + 1]))

    maps: list[list[tuple[range, range, int]]] = []  # change tuple to single list
    m = []
    for i in range(2, len(input)):
        line = input[i].strip()
        if line != "" and line[0].isdigit():
            nums = [int(x) for x in line.split(" ")]
            dst = range(nums[0], nums[0] + nums[2])
            src = range(nums[1], nums[1] + nums[2])
            m.append((dst, src, nums[1] - nums[0]))
        elif len(m) > 0:
            maps.append(m)
            m = []
    maps.append(m)

    result = None

    # 1. filter seeds by intersection
    # 2. operation
    # 3. filter seeds by intersection
    # 4. operation
    for seeds in seeds_ranges:
        for seed in seeds:
            mapped_value = seed
            # for m in maps:
            #     for dst, src, dif in m:
            #         if mapped_value in src:
            #             mapped_value -= dif
            #             break
            # if not result or mapped_value < result:
            #     result = mapped_value
    print(f"part 2: {result}")


def part_1(input: list[str]):
    seeds = [int(x) for x in input[0].split(":")[1].strip().split(" ")]

    maps: list[list[tuple[range, range, int]]] = []  # change tuple to single list
    m = []
    for i in range(2, len(input)):
        line = input[i].strip()
        if line != "" and line[0].isdigit():
            nums = [int(x) for x in line.split(" ")]
            dst = range(nums[0], nums[0] + nums[2])
            src = range(nums[1], nums[1] + nums[2])
            m.append((dst, src, nums[1] - nums[0]))
        elif len(m) > 0:
            maps.append(m)
            m = []
    maps.append(m)

    results = []
    for seed in seeds:
        mapped_value = seed
        for m in maps:
            for dst, src, dif in m:
                if mapped_value in src:
                    mapped_value -= dif
                    break
        results.append(mapped_value)
    print(f"part 1: {min(results)}")


def intersect(x: range, y: range) -> range:
    return range(max(x[0], y[0]), min(x[-1], y[-1]) + 1)


def run():
    input = get_input(5).splitlines()
    part_1(input)
    part_2(input)


test_input = """
seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4
""".strip()
