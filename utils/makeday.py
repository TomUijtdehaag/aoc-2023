from argparse import ArgumentParser

from templates import day_template, test_template


def main():
    parser = ArgumentParser()
    parser.add_argument("day", help="The day to create", type=int)
    args = parser.parse_args()
    day = args.day
    print(f"Creating day {day}")
    with open(f"input/{day}.txt", "w") as f:
        f.write("")

    with open(f"d{day}.py", "w") as f:
        f.write(day_template.format(day=day))

    with open(f"tests/test_d{day}.py", "w") as f:
        f.write(test_template.format(day=day))


if __name__ == "__main__":
    main()
