from d8 import Graph, Node, one, two

test_input = """RL

AAA = (BBB, CCC)
BBB = (DDD, EEE)
CCC = (ZZZ, GGG)
DDD = (DDD, DDD)
EEE = (EEE, EEE)
GGG = (GGG, GGG)
ZZZ = (ZZZ, ZZZ)""".splitlines()

test_input_2 = """LLR

AAA = (BBB, BBB)
BBB = (AAA, ZZZ)
ZZZ = (ZZZ, ZZZ)""".splitlines()


test_input_3 = """LR

11A = (11B, XXX)
11B = (XXX, 11Z)
11Z = (11B, XXX)
22A = (22B, XXX)
22B = (22C, 22C)
22C = (22Z, 22Z)
22Z = (22B, 22B)
XXX = (XXX, XXX)""".splitlines()


def test_parse():
    assert Graph.parse(test_input) == Graph(
        "RL",
        {
            "AAA": Node("AAA", "BBB", "CCC"),
            "BBB": Node("BBB", "DDD", "EEE"),
            "CCC": Node("CCC", "ZZZ", "GGG"),
            "DDD": Node("DDD", "DDD", "DDD"),
            "EEE": Node("EEE", "EEE", "EEE"),
            "GGG": Node("GGG", "GGG", "GGG"),
            "ZZZ": Node("ZZZ", "ZZZ", "ZZZ"),
        },
    )


def test_one():
    graph = Graph.parse(test_input)
    assert one(graph) == 2


def test_one_2():
    graph = Graph.parse(test_input_2)
    assert one(graph) == 6


def test_two():
    graph = Graph.parse(test_input_3)
    assert two(graph) == 6
