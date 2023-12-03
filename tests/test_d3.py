from d3 import Part, Position, Schematic, Symbol, one, two

test_input = """467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..""".splitlines()


class TestSchematic:
    s = Schematic(test_input)

    def test_init(self):
        assert self.s.width == 10
        assert self.s.height == 10

    def test_find_parts_line(self):
        assert self.s.find_parts_line("467..114..", 0) == [
            Part(467, (Position(0, 0), Position(1, 0), Position(2, 0))),
            Part(114, (Position(5, 0), Position(6, 0), Position(7, 0))),
        ]

    def test_get_neighbors(self):
        assert self.s.get_neighbors(Position(0, 0)) == set(
            [Part(467, (Position(0, 0), Position(1, 0), Position(2, 0)))]
        )

        assert self.s.get_neighbors(Position(2, 0)) == set(
            [
                Part(467, (Position(0, 0), Position(1, 0), Position(2, 0))),
                Symbol("*", Position(3, 1)),
            ]
        )

    def test_get_adjacent_symbols(self):
        assert self.s.get_adjacent_symbols(
            Part(467, (Position(0, 0), Position(1, 0), Position(2, 0)))
        ) == set([Symbol("*", Position(3, 1))])

    def test_get_adjacent_parts(self):
        assert self.s.get_adjacent_parts(Symbol("*", Position(3, 1))) == set(
            [
                Part(35, (Position(2, 2), Position(3, 2))),
                Part(467, (Position(0, 0), Position(1, 0), Position(2, 0))),
            ]
        )


class TestPart:
    parts = [
        Part(467, (Position(0, 0), Position(1, 0), Position(2, 0))),
        Part(114, (Position(5, 0), Position(6, 0), Position(7, 0))),
    ]

    def test_add(self):
        assert self.parts[0] + self.parts[1] == 467 + 114

    def test_sum(self):
        assert sum(self.parts) == 467 + 114

    def test_mul(self):
        assert self.parts[0] * self.parts[1] == 467 * 114


def test_one():
    schematic = Schematic(test_input)
    assert one(schematic) == 4361


def test_two():
    schematic = Schematic(test_input)
    assert two(schematic) == 467835
