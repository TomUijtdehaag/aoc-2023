from utils.read import read


def parse(input: str):
    times, distances = input.split("\n")
    times = [int(t) for t in times.split()[1:] if t != ""]
    distances = [int(d) for d in distances.split()[1:] if d != ""]
    return [(t, d) for t, d in zip(times, distances)]


def parse_two(input: str):
    times, distances = input.split("\n")
    time = int(times.replace("Time:", "").replace(" ", ""))
    distance = int(distances.replace("Distance:", "").replace(" ", ""))

    return time, distance


def get_distances(time):
    distances = []
    for hold in range(time):
        distances.append(hold * (time - hold))

    return distances


def get_number_of_wins(time, distance):
    distances = get_distances(time)
    return len([d for d in distances if d > distance])


def one(inputs: list[tuple[int, int]]):
    out = 1
    for t, d in inputs:
        out *= get_number_of_wins(t, d)

    return out


def two(input: tuple[int, int]):
    time, distance = input
    return get_number_of_wins(time, distance)


if __name__ == "__main__":
    input = read("input/6.txt")
    inputs = parse(input)

    print("Part one:", one(inputs))

    in_two = parse_two(input)
    print("Part two:", two(in_two))
