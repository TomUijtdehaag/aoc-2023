from tqdm import tqdm

from utils.read import readlines


class Range:
    def __init__(self, dest: int, source: int, length: int):
        self.source_range = range(source, source + length)
        self.dest_range = range(dest, dest + length)
        self.offset = dest - source

    def forward(self, n: int):
        return n + self.offset

    def reverse(self, n: int):
        return n - self.offset

    def __repr__(self):
        s = ""
        for n in self.range:
            s += f"{n} -> {n + self.offset}\n"

        return s

    def __eq__(self, other):
        return (
            self.source_range == other.source_range
            and self.dest_range == other.dest_range
            and self.offset == other.offset
        )


class Map:
    def __init__(self, name: str, ranges: list[Range]):
        self.name = name
        self.ranges = ranges

    def forward(self, n: int):
        for r in self.ranges:
            if n in r.source_range:
                return r.forward(n)

        return n

    def reverse(self, n: int):
        for r in self.ranges:
            if n in r.dest_range:
                return r.reverse(n)

        return n


def parse(lines: list[str]) -> tuple[list[int], list[Map]]:
    seeds = [int(n) for n in lines[0].split(":")[-1].strip().split()]
    maps = []
    ranges = []

    for line in lines[2:]:
        if "map" in line:
            map_name = line.split()[0]

        elif line.strip() == "":
            maps.append(Map(map_name, ranges))
            ranges = []

        else:
            dest, source, length = line.split()
            ranges.append(Range(int(dest), int(source), int(length)))

    else:
        maps.append(Map(map_name, ranges))

    return seeds, maps


def one(seeds: list[int], maps: list[Map]):
    locations = []

    for seed in seeds:
        for map in maps:
            seed = map.forward(seed)

        locations.append(seed)

    return min(locations)


def two(seeds: list[int], maps: list[Map]):
    seeds_ranges = [
        range(start, start + length) for start, length in zip(seeds[::2], seeds[1::2])
    ]

    max_location = max([r.dest_range.stop for r in maps[-1].ranges])

    for location in tqdm(range(max_location)):
        seed = location
        for map in maps[::-1]:
            seed = map.reverse(seed)

        if any(seed in r for r in seeds_ranges):
            return location


if __name__ == "__main__":
    lines = readlines("input/5.txt")
    seeds, maps = parse(lines)

    print("Part one:", one(seeds, maps))
    print("Part two:", two(seeds, maps))
