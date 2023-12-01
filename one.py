import re

from utils.read import readlines


def one(lines: list[str]) -> int:
    numbers = [int(filter_numbers(line)) for line in lines]

    return sum(numbers)


def filter_numbers(line: str) -> int:
    digit_list = [char for char in line if char.isdigit()]
    digits = "".join([digit_list[0], digit_list[-1]])
    return int(digits)


DIGIT_MAP = dict(
    zip(
        "one, two, three, four, five, six, seven, eight, nine".split(", "), range(1, 10)
    )
)


def convert_to_number(line: str) -> int:
    digits = {}
    for word, digit in DIGIT_MAP.items():
        matches = re.finditer(word, line)

        for match in matches:
            digits[match.start()] = str(digit)

    for i, char in enumerate(line):
        if char.isdigit():
            digits[i] = char

    digit_list = sorted(digits.items(), key=lambda x: x[0])
    number = digit_list[0][1] + digit_list[-1][1]

    return int(number)


def two(lines: list[str]) -> int:
    numbers = []

    for line in lines:
        number = convert_to_number(line)
        numbers.append(number)

    return sum(numbers)


if __name__ == "__main__":
    input = readlines("input/1.txt")

    print("Part one:", one(input))
    print("Part two:", two(input))
