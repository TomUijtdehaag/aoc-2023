from utils.read import readlines

BAG = {"red": 12, "green": 13, "blue": 14}


def parse(line: str) -> tuple[int, list[dict[str, int]]]:
    game_id, game = line.split(":")
    game_id = int(game_id.split(" ")[1])

    games = game.split(";")

    sets = []
    for game in games:
        set = {}
        for amount_color in game.split(","):
            amount, color = amount_color.strip().split(" ")
            set[color] = int(amount)
        sets.append(set)

    return game_id, sets


def is_possible(game: list[dict[str, int]], bag: dict[str, int]) -> bool:
    for set in game:
        for color, amount in set.items():
            if amount > bag[color]:
                return False

    return True


def possible_sum(games: list[tuple[int, list[dict[str, int]]]]) -> int:
    return sum(game_id for game_id, game in games if is_possible(game, BAG))


def one():
    games = [parse(line) for line in readlines("input/2.txt")]
    return possible_sum(games)


def min_cubes(game: list[dict[str, int]]) -> dict[str, int]:
    min_cubes = {}
    for set in game:
        for color, amount in set.items():
            if color not in min_cubes or amount > min_cubes[color]:
                min_cubes[color] = amount

    return min_cubes


def power(min_cubes: dict[str, int]) -> int:
    p = 1
    for amount in min_cubes.values():
        p *= amount

    return p


def two():
    games = [parse(line) for line in readlines("input/2.txt")]
    return sum([power(min_cubes(game)) for _, game in games])


if __name__ == "__main__":
    print("part one:", one())
    print("part two:", two())
