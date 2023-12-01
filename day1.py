from typing import Optional

from util import get_input

written = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}


class CalibrationValue:
    def __init__(self):
        self.left = None
        self.right = None

    def put(self, value: int):
        if not self.left:
            self.left = value
        else:
            self.right = value

    def as_int(self) -> int:
        buffer = ""
        if self.left:
            buffer += str(self.left)
        else:
            raise Exception("Number not initialized")
        if self.right:
            buffer += str(self.right)
        else:
            buffer += str(self.left)
        return int(buffer)


def get_written_digit(s: str) -> Optional[int]:
    buffer = ""
    end = min(5, len(s))
    for j in range(end):
        buffer += s[j]
        if written.get(buffer):
            return written.get(buffer)
    return None


def get_calibration_value(line: str, contains_written: bool) -> int:
    value = CalibrationValue()
    for i in range(len(line)):
        if line[i].isdigit():
            value.put(int(line[i]))
        elif contains_written:
            spelled_digit = get_written_digit(line[i:])
            if spelled_digit:
                value.put(spelled_digit)
    return value.as_int()


def part_1():
    input = get_input(1)
    numbers = []
    for line in input.splitlines():
        numbers.append(get_calibration_value(line, False))
    print(f"part_1: {sum(numbers)}")


def part_2():
    input = get_input(1)
    numbers = []
    for line in input.splitlines():
        numbers.append(get_calibration_value(line, True))
    print(f"part_2: {sum(numbers)}")


def run():
    part_1()
    part_2()
