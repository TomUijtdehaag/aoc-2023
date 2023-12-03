import re
from dataclasses import dataclass

from utils.read import readlines


@dataclass(frozen=True)
class Position:
    x: int
    y: int


@dataclass(frozen=True)
class Part:
    number: int
    positions: tuple[Position]

    def __add__(self, other):
        if isinstance(other, int):
            return self.number + other
        else:
            return self.number + other.number

    def __radd__(self, other):
        if isinstance(other, int):
            return self.number + other
        else:
            return self.number + other.number

    def __mul__(self, other):
        if isinstance(other, int):
            return self.number * other
        else:
            return self.number * other.number

    def __rmul__(self, other):
        if isinstance(other, int):
            return self.number * other
        else:
            return self.number * other.number


@dataclass(frozen=True)
class Symbol:
    char: str
    position: Position


class Schematic:
    def __init__(self, schematic: list[str]):
        self.schematic = schematic
        self.width = len(schematic[0])
        self.height = len(schematic)

        self.map, self.symbols = self.make_map()
        self.parts = self.find_parts(self.schematic)

    def find_parts(self, schematic: list[str]) -> list[Part]:
        parts = []
        for y, line in enumerate(schematic):
            parts.extend(self.find_parts_line(line, y))

        return parts

    def find_parts_line(self, line: str, y: int) -> list[Part]:
        parts = []
        matches = re.finditer(r"[0-9]+", line)

        for match in matches:
            positions = tuple(Position(x, y) for x in range(match.start(), match.end()))

            part = Part(int(match.group()), positions)
            for position in positions:
                self.map[position.y][position.x] = part

            parts.append(part)

        return parts

    def make_map(self):
        map = []
        symbols = []

        for y in range(self.height):
            line = []
            for x in range(self.width):
                char = self.schematic[y][x]
                if char.isnumeric() or char == ".":
                    line.append(None)
                else:
                    symbol = Symbol(char, Position(x, y))
                    line.append(symbol)
                    symbols.append(symbol)

            map.append(line)

        return map, symbols

    def get_neighbors(self, position: Position) -> set[Part]:
        above = max([position.y - 1, 0])
        left = max([position.x - 1, 0])
        right = min([position.x + 2, self.width])
        below = min([position.y + 2, self.height])

        neighbors = set()

        for y in range(above, below):
            for x in range(left, right):
                if self.map[y][x] is not None:
                    neighbors.add(self.map[y][x])

        return neighbors

    def get_adjacent_symbols(self, part: Part) -> list[Symbol]:
        neighbors = set()

        for position in part.positions:
            neighbors.update(self.get_neighbors(position))

        return set([neighbor for neighbor in neighbors if isinstance(neighbor, Symbol)])

    def get_adjacent_parts(self, symbol: Symbol) -> list[Part]:
        neighbors = self.get_neighbors(symbol.position)

        return [neighbor for neighbor in neighbors if isinstance(neighbor, Part)]


def one(s: Schematic):
    parts = [part for part in s.parts if len(s.get_adjacent_symbols(part)) > 0]
    return sum(parts)


def two(s: Schematic):
    gears = [
        symbol
        for symbol in s.symbols
        if symbol.char == "*" and len(s.get_adjacent_parts(symbol)) == 2
    ]

    return sum(
        [
            parts[0] * parts[1]
            for parts in [s.get_adjacent_parts(gear) for gear in gears]
        ]
    )


if __name__ == "__main__":
    schematic = readlines("input/3.txt")
    s = Schematic(schematic)

    print("part one:", one(s))
    print("part two:", two(s))
