import os
import os.path

import requests as requests


def get_input(day: int) -> str:
    file_path = get_file_path(day)
    if os.path.exists(file_path):
        return read_from_file(file_path)
    else:
        txt = download_input(day)
        write_to_file(file_path, txt)
        return txt


def download_input(day: int, year: int = 2023) -> str:
    response = requests.get(
        url=f"https://adventofcode.com/{year}/day/{day}/input",
        cookies={"session": os.getenv("SESSION")}
    )
    response.raise_for_status()
    return response.text.strip()


def write_to_file(file_path: str, txt: str):
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    with open(file_path, 'w') as file:
        file.write(txt)
    pass


def read_from_file(file_path) -> str:
    with open(file_path, 'r') as file:
        return file.read()


def get_file_path(day: int) -> str:
    return os.getcwd() + f"/input/day_{day}.txt"
