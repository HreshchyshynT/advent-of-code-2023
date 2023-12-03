# This is a sample Python script.

import day1
import day2
from dotenv import load_dotenv

import day3

if __name__ == '__main__':
    load_dotenv()
    print("day 1")
    day1.run()
    print("day 2")
    day2.run()
    print("day 3")
    day3.run()
