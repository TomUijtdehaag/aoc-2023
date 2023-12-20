from d11 import solve

test_input = """...#......
.......#..
#.........
..........
......#...
.#........
.........#
..........
.......#..
#...#.....""".splitlines()


def test_one():
    assert solve(test_input, 2) == 374


def test_two():
    assert solve(test_input, factor=10) == 1030
    assert solve(test_input, factor=100) == 8410
