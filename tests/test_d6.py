from d6 import one, parse, parse_two, two

test_input = """Time:      7  15   30
Distance:  9  40  200"""


def test_parse():
    assert parse(test_input) == [
        (7, 9),
        (15, 40),
        (30, 200),
    ]


def test_one():
    assert one(parse(test_input)) == 288


def test_two():
    assert two(parse_two(test_input)) == 71503
