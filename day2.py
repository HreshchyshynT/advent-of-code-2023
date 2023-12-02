from util import get_input


def part_1():
    ids = []
    for line in get_input(2).splitlines():
        s = line.split(":")
        subsets = s[1].split(";")
        save = True
        for subset in subsets:
            red_limit = 12
            green_limit = 13
            blue_limit = 14
            for cube_str in subset.split(","):
                cube = cube_str.split(" ")
                color = cube[2]
                count = int(cube[1])
                if color == "green":
                    green_limit -= count
                elif color == "red":
                    red_limit -= count
                elif color == "blue":
                    blue_limit -= count
            if red_limit < 0 or green_limit < 0 or blue_limit < 0:
                save = False
                break
        if save:
            ids.append(int(s[0].split(" ")[1]))
    print(f"part 1: {sum(ids)}")


def part_2():
    powers = []
    for line in get_input(2).splitlines():
        s = line.split(":")
        subsets = s[1].split(";")
        r = 0
        g = 0
        b = 0
        for subset in subsets:
            s_r = 0
            s_g = 0
            s_b = 0
            for cube_str in subset.split(","):
                cube = cube_str.split(" ")
                color = cube[2]
                count = int(cube[1])
                if color == "green":
                    s_g += count
                elif color == "red":
                    s_r += count
                elif color == "blue":
                    s_b += count
            if s_r > r:
                r = s_r
            if s_g > g:
                g = s_g
            if s_b > b:
                b = s_b

        powers.append(r * g * b)

    print(f"part 1: {sum(powers)}")


def run():
    part_1()
    part_2()
