from d9 import diffs, one, parse, solve_one, two

test_input = """0 3 6 9 12 15
1 3 6 10 15 21
10 13 16 21 30 45""".splitlines()


def test_parse():
    inputs = parse(test_input)
    assert inputs[0] == [0, 3, 6, 9, 12, 15]
    assert inputs[1] == [1, 3, 6, 10, 15, 21]
    assert inputs[2] == [10, 13, 16, 21, 30, 45]


def test_diffs():
    assert diffs([0, 3, 6, 9, 12, 15]) == [3, 3, 3, 3, 3]
    assert diffs([1, 3, 6, 10, 15, 21]) == [2, 3, 4, 5, 6]
    assert diffs([10, 13, 16, 21, 30, 45]) == [3, 3, 5, 9, 15]


def test_solve_one():
    assert solve_one([0, 3, 6, 9, 12, 15]) == 18
    assert solve_one([1, 3, 6, 10, 15, 21]) == 28
    assert solve_one([10, 13, 16, 21, 30, 45]) == 68


def test_one():
    sequences = parse(test_input)
    assert one(sequences) == 114


def test_two():
    sequences = parse(test_input)
    assert two(sequences) == 2
