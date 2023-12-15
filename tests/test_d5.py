from d5 import Range, one, parse, two

test_input = """seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4""".splitlines()


def test_parse():
    seeds, maps = parse(test_input)
    assert seeds == [79, 14, 55, 13]
    assert maps[0].name == "seed-to-soil"
    assert maps[0].ranges == [
        Range(50, 98, 2),
        Range(52, 50, 48),
    ]
    assert maps[1].name == "soil-to-fertilizer"
    assert maps[1].ranges == [
        Range(0, 15, 37),
        Range(37, 52, 2),
        Range(39, 0, 15),
    ]
    assert maps[2].name == "fertilizer-to-water"
    assert maps[2].ranges == [
        Range(49, 53, 8),
        Range(0, 11, 42),
        Range(42, 0, 7),
        Range(57, 7, 4),
    ]
    assert maps[3].name == "water-to-light"
    assert maps[3].ranges == [
        Range(88, 18, 7),
        Range(18, 25, 70),
    ]
    assert maps[4].name == "light-to-temperature"
    assert maps[4].ranges == [
        Range(45, 77, 23),
        Range(81, 45, 19),
        Range(68, 64, 13),
    ]
    assert maps[5].name == "temperature-to-humidity"
    assert maps[5].ranges == [
        Range(0, 69, 1),
        Range(1, 0, 69),
    ]
    assert maps[6].name == "humidity-to-location"
    assert maps[6].ranges == [
        Range(60, 56, 37),
        Range(56, 93, 4),
    ]


class TestMap:
    def test_forward(self):
        seeds, maps = parse(test_input)

        test_values = [
            [81, 81, 81, 74, 78, 78, 82],
            [14, 53, 49, 42, 42, 43, 43],
            [57, 57, 53, 46, 82, 82, 86],
            [13, 52, 41, 34, 34, 35, 35],
        ]

        for s, seed in enumerate(seeds):
            for m, map in enumerate(maps):
                seed = map.forward(seed)
                assert seed == test_values[s][m]


def test_one():
    seeds, maps = parse(test_input)
    assert one(seeds, maps) == 35


def test_two():
    seeds, maps = parse(test_input)
    assert two(seeds, maps) == 46
