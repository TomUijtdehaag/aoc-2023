from dataclasses import dataclass

from utils.read import readlines


@dataclass
class Tile:
    x: int
    y: int
    type: str = "."

    def is_connected(self, direction: str):
        return False

    def __hash__(self) -> int:
        return hash((self.x, self.y))


class Pipe(Tile):
    def __init__(self, x: int, y: int, type: str) -> None:
        super().__init__(x, y, type)
        self.connections = list(self._connections())
        self.in_ = None
        self.out = None
        self.c = None

    def is_connected(self, direction: str):
        if direction == "north":
            return self.type in "J|LS"

        if direction == "east":
            return self.type in "LF-S"

        if direction == "south":
            return self.type in "7|FS"

        if direction == "west":
            return self.type in "7-JS"

    def is_connected_opposite(self, direction: str):
        directions = ["north", "east", "south", "west"]

        return self.is_connected(directions[(directions.index(direction) + 2) % 4])

    def _connections(self):
        for direction in ["north", "east", "south", "west"]:
            if self.is_connected(direction):
                yield direction


class Map:
    def __init__(self, input: list[str]) -> None:
        self._parse(input)
        self._connect()

    def _parse(self, input: list[str]):
        self.tiles = []
        for y, line in enumerate(input):
            row = []
            for x, char in enumerate(line):
                if char == ".":
                    row.append(Tile(x, y))
                else:
                    row.append(Pipe(x, y, char))

            self.tiles.append(row)

    def _connect(self):
        start = self.find_start()
        pipe = start

        pipes = []
        while True:
            pipes.append(pipe)

            if pipe.type == "S" and len(pipes) > 1:
                break

            for direction in pipe._connections():
                tile = self._get_tile_direction(direction, pipe.x, pipe.y)
                if (
                    tile
                    and isinstance(tile, Pipe)
                    and (tile.x, tile.y) != pipe.in_
                    and tile.is_connected_opposite(direction)
                ):
                    pipe.out = (tile.x, tile.y)
                    tile.in_ = (pipe.x, pipe.y)
                    pipe = tile
                    break

        self.pipes = pipes

    def find_start(self):
        for row in self.tiles:
            for tile in row:
                if isinstance(tile, Pipe) and tile.type == "S":
                    return tile
        return None

    def _get_tile(self, x, y) -> Pipe | Tile:
        if x < 0 or y < 0:
            return None
        if x >= len(self.tiles[0]) or y >= len(self.tiles):
            return None

        try:
            return self.tiles[y][x]
        except IndexError:
            return None

    def _get_tile_direction(self, direction: str, x, y) -> Pipe | Tile:
        if direction == "north":
            return self._get_tile(x, y - 1)

        if direction == "east":
            return self._get_tile(x + 1, y)

        if direction == "south":
            return self._get_tile(x, y + 1)

        if direction == "west":
            return self._get_tile(x - 1, y)

    def draw_map(self):
        for row in self.tiles:
            for tile in row:
                if tile in self.pipes:
                    print(tile.type, end="")
                else:
                    print(".", end="")
            print()

    def count_area(self):
        pipes = set(self.pipes)
        area = 0
        for row in self.tiles:
            inside = False
            for tile in row:
                if tile in pipes:
                    if tile.type in "|JL":
                        inside = not inside
                else:
                    area += inside

        return area


def one(map: Map):
    return (len(map.pipes)) // 2


def two(map: Map):
    return map.count_area()


if __name__ == "__main__":
    lines = readlines("input/10.txt")
    map = Map(lines)

    print("Part one:", one(map))
    print("Part two:", two(map))
