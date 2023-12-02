from d2 import BAG, is_possible, min_cubes, parse, power

test_input = """Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green""".split("\n")


def test_parse():
    assert parse(test_input[0]) == (
        1,
        [{"blue": 3, "red": 4}, {"red": 1, "green": 2, "blue": 6}, {"green": 2}],
    )

    assert parse(test_input[1]) == (
        2,
        [
            {"blue": 1, "green": 2},
            {"green": 3, "blue": 4, "red": 1},
            {"green": 1, "blue": 1},
        ],
    )

    assert parse(test_input[2]) == (
        3,
        [
            {"green": 8, "blue": 6, "red": 20},
            {"blue": 5, "red": 4, "green": 13},
            {"green": 5, "red": 1},
        ],
    )


def test_is_possible():
    values = [True, True, False, False, True]

    for i in range(5):
        assert is_possible(parse(test_input[i])[1], BAG) == values[i]


def test_min_cubes():
    values = [
        {"red": 4, "green": 2, "blue": 6},
        {"red": 1, "green": 3, "blue": 4},
        {"red": 20, "green": 13, "blue": 6},
        {"red": 14, "green": 3, "blue": 15},
        {"red": 6, "green": 3, "blue": 2},
    ]

    for i in range(5):
        assert min_cubes(parse(test_input[i])[1]) == values[i]


def test_power():
    values = [48, 12, 1560, 630, 36]

    for i in range(5):
        assert power(min_cubes(parse(test_input[i])[1])) == values[i]


def test_two():
    assert (
        sum(
            [power(min_cubes(game)) for _, game in [parse(line) for line in test_input]]
        )
        == 2286
    )
