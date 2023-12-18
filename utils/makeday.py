import os
from argparse import ArgumentParser

import requests
from dotenv import load_dotenv
from templates import day_template, test_template

load_dotenv()


def main():
    parser = ArgumentParser()
    parser.add_argument("day", help="The day to create", type=int)
    parser.add_argument("--year", help="The year to create", type=int, default=2023)
    args = parser.parse_args()
    day = args.day
    year = args.year
    print(f"Creating day {day}")
    with open(f"input/{day}.txt", "w") as f:
        input = requests.get(
            f"https://adventofcode.com/{year}/day/{day}/input",
            cookies={
                "session": os.getenv("AOC_SESSION")  # get session from browser request
            },
        ).text
        f.write(input)

    with open(f"d{day}.py", "w") as f:
        f.write(day_template.format(day=day))

    with open(f"tests/test_d{day}.py", "w") as f:
        f.write(test_template.format(day=day))


if __name__ == "__main__":
    main()
