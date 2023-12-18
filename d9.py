from utils.read import readlines


def parse(input: list[str]):
    return [[int(num) for num in line.split()] for line in input]


def diffs(sequence: list[int]):
    return [sequence[i + 1] - sequence[i] for i in range(len(sequence) - 1)]


def solve_one(sequence):
    diff = diffs(sequence)

    if not any(diff):
        return sequence[-1] + diff[-1]

    return sequence[-1] + solve_one(diff)


def solve_two(sequence):
    diff = diffs(sequence)

    if not any(diff):
        return sequence[0] - diff[0]

    return sequence[0] - solve_two(diff)


def one(sequences):
    values = []
    for sequence in sequences:
        values.append(solve_one(sequence))

    return sum(values)


def two(sequences):
    values = []
    for sequence in sequences:
        values.append(solve_two(sequence))

    return sum(values)


if __name__ == "__main__":
    lines = readlines("input/9.txt")
    sequences = parse(lines)

    print("Part one:", one(sequences))
    print("Part two:", two(sequences))
