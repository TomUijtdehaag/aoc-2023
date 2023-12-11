from d4 import Card, copies, one, parse, two

test_input = """Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11""".splitlines()


def test_parse():
    cards = [parse(line) for line in test_input]
    assert cards[0] == Card(
        card=1,
        winning_numbers=[41, 48, 83, 86, 17],
        your_numbers=[83, 86, 6, 31, 17, 9, 48, 53],
    )
    assert cards[1] == Card(
        card=2,
        winning_numbers=[13, 32, 20, 16, 61],
        your_numbers=[61, 30, 68, 82, 17, 32, 24, 19],
    )
    assert cards[2] == Card(
        card=3,
        winning_numbers=[1, 21, 53, 59, 44],
        your_numbers=[69, 82, 63, 72, 16, 21, 14, 1],
    )
    assert cards[3] == Card(
        card=4,
        winning_numbers=[41, 92, 73, 84, 69],
        your_numbers=[59, 84, 76, 51, 58, 5, 54, 83],
    )
    assert cards[4] == Card(
        card=5,
        winning_numbers=[87, 83, 26, 28, 32],
        your_numbers=[88, 30, 70, 12, 93, 22, 82, 36],
    )
    assert cards[5] == Card(
        card=6,
        winning_numbers=[31, 18, 13, 56, 72],
        your_numbers=[74, 77, 10, 23, 35, 67, 36, 11],
    )


def test_value():
    cards = [parse(line) for line in test_input]
    assert cards[0].value() == 8
    assert cards[1].value() == 2
    assert cards[2].value() == 2
    assert cards[3].value() == 1
    assert cards[4].value() == 0
    assert cards[5].value() == 0


def test_one():
    cards = [parse(line) for line in test_input]
    assert one(cards) == 13


def test_copies():
    cards = [parse(line) for line in test_input]
    assert copies(cards) == {1: 1, 2: 2, 3: 4, 4: 8, 5: 14, 6: 1}


def test_two():
    cards = [parse(line) for line in test_input]
    assert two(cards) == 30
