from utils.read import readlines


def get_empty_rows(map: list[str]):
    for i, row in enumerate(map):
        if all(c == "." for c in row):
            yield i


def get_empty_cols(map: list[str]):
    for i, col in enumerate(zip(*map)):
        if all(c == "." for c in col):
            yield i


def find_galaxies(map: list[str]):
    galaxies = {}
    n = 1
    for y, row in enumerate(map):
        for x, col in enumerate(row):
            if col == "#":
                galaxies[n] = (x, y)
                n += 1

    return galaxies


def expand_galaxies(
    galaxies: dict[int, tuple[int, int]],
    empty_rows: list[int],
    empty_cols: list[int],
    factor: int,
):
    factor = factor - 1
    for galaxy, (x, y) in galaxies.items():
        row_exp = [i for i in empty_rows if i < y]
        col_exp = [i for i in empty_cols if i < x]

        galaxies[galaxy] = (
            x + len(col_exp) * factor,
            y + len(row_exp) * factor,
        )

    return galaxies


def get_combinations(galaxies: dict[int, tuple[int, int]]):
    galaxies = list(galaxies.keys())

    for i, a in enumerate(galaxies):
        for b in galaxies[i + 1 :]:
            yield a, b


def calculate_distance(galaxies: dict[int, tuple[int, int]], a: int, b: int):
    xa, ya = galaxies[a]
    xb, yb = galaxies[b]
    return abs(xa - xb) + abs(ya - yb)


def solve(map: list[str], factor: int):
    empty_rows = list(get_empty_rows(map))
    empty_cols = list(get_empty_cols(map))

    galaxies = find_galaxies(map)
    galaxies = expand_galaxies(galaxies, empty_rows, empty_cols, factor)

    distances = []
    for a, b in get_combinations(galaxies):
        distances.append(calculate_distance(galaxies, a, b))

    return sum(distances)


if __name__ == "__main__":
    lines = readlines("input/11.txt")

    print("Part one:", solve(lines, 2))
    print("Part two:", solve(lines, 1_000_000))
