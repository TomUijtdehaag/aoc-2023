from d10 import Map, Pipe, one, two

test_input = """..F7.
.FJ|.
SJ.L7
|F--J
LJ...""".splitlines()

test_input_2 = """FF7FSF7F7F7F7F7F---7
L|LJ||||||||||||F--J
FL-7LJLJ||||||LJL-77
F--JF--7||LJLJ7F7FJ-
L---JF-JLJ.||-FJLJJ7
|F|F-JF---7F7-L7L|7|
|FFJF7L7F-JF7|JL---7
7-L-JL7||F7|L7F-7F7|
L.L7LFJ|||||FJL7||LJ
L7JLJL-JLJLJL--JLJ.L""".splitlines()


class TestPipe:
    def test_is_connected(self):
        pipe = Pipe(1, 1, "F")
        assert not pipe.is_connected("north")
        assert pipe.is_connected("east")
        assert pipe.is_connected("south")
        assert not pipe.is_connected("west")


class TestMap:
    def test_parse(self):
        map = Map(test_input)
        assert len(map.tiles) == 25
        assert map.tiles[0].x == 0
        assert map.tiles[0].y == 0
        assert map.tiles[0].type == "."
        assert map.tiles[1].x == 1
        assert map.tiles[1].y == 0
        assert map.tiles[1].type == "."
        assert map.tiles[2].x == 2
        assert map.tiles[2].y == 0
        assert map.tiles[2].type == "F"

    def test_connect(self):
        pass

    def test_find_start(self):
        map = Map(test_input)

        start = map.find_start()
        assert start.type == "S"
        assert start.x == 0
        assert start.y == 2


def test_one():
    map = Map(test_input)
    assert one(map) == 8


def test_two():
    map = Map(test_input_2)
    assert two(map) == 10
