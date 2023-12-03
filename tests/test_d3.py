from d3 import Part, Position, Schematic, Symbol

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


def test_schematic():
    schematic = Schematic(test_input)
    assert schematic.width == 10
    assert schematic.height == 10

    assert schematic.find_parts_line("467..114..", 0) == [
        Part(467, (Position(0, 0), Position(1, 0), Position(2, 0))),
        Part(114, (Position(5, 0), Position(6, 0), Position(7, 0))),
    ]

    assert schematic.get_neighbors(Position(0, 0)) == set(
        [Part(467, (Position(0, 0), Position(1, 0), Position(2, 0)))]
    )

    assert schematic.get_neighbors(Position(2, 0)) == set(
        [
            Part(467, (Position(0, 0), Position(1, 0), Position(2, 0))),
            Symbol("*", Position(3, 1)),
        ]
    )

    assert schematic.get_adjacent_symbols(
        Part(467, (Position(0, 0), Position(1, 0), Position(2, 0)))
    ) == set([Symbol("*", Position(3, 1))])

    assert schematic.get_adjacent_parts(Symbol("*", Position(3, 1))) == [
        Part(35, (Position(2, 2), Position(3, 2))),
        Part(467, (Position(0, 0), Position(1, 0), Position(2, 0))),
    ]

    assert (
        Part(467, (Position(0, 0), Position(1, 0), Position(2, 0)))
        + Part(114, (Position(5, 0), Position(6, 0), Position(7, 0)))
        == 467 + 114
    )
