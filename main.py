# This is a sample Python script.
from typing import Optional

import day1

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

spelled = {
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


class Number:
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


def read_digit(s: str) -> Optional[int]:
    buffer = ""
    end = min(5, len(s))
    for j in range(end):
        buffer += s[j]
        if spelled.get(buffer):
            return spelled.get(buffer)
    return None


def get_number(line: str) -> int:
    number = Number()
    for i in range(len(line)):
        if line[i].isdigit():
            number.put(int(line[i]))
        else:
            spelled_digit = read_digit(line[i:])
            if spelled_digit:
                number.put(spelled_digit)
    return number.as_int()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    day1.run()
