# This is a sample Python script.

import day1
import day2
from dotenv import load_dotenv

if __name__ == '__main__':
    load_dotenv()
    print("day 1")
    day1.run()
    print("day 2")
    day2.run()
