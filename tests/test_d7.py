from d7 import Card, Hand, one, parse

test_input = """32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483""".splitlines()


class TestCard:
    def test_eq(self):
        assert Card("3") == Card("3")
        assert Card("3") != Card("4")

    def test_lt(self):
        assert Card("4") < Card("3")

    def test_gt(self):
        assert Card("3") > Card("4")


def test_parse():
    hands = parse(test_input)

    assert hands[0].cards == [Card("3"), Card("2"), Card("T"), Card("3"), Card("K")]
    assert hands[0].bid == 765
    assert hands[0].type == Hand.Types.ONE_PAIR

    assert hands[1].cards == [Card("T"), Card("5"), Card("5"), Card("J"), Card("5")]
    assert hands[1].bid == 684
    assert hands[1].type == Hand.Types.THREE_OF_A_KIND


class TestHand:
    hand_a = Hand("33332")
    hand_b = Hand("2AAAA")
    hand_c = Hand("77888")
    hand_d = Hand("77788")

    hands = parse(test_input, True)

    def test_lt(self):
        assert self.hand_a < self.hand_b
        assert self.hand_c < self.hand_d

    def test_gt(self):
        assert self.hand_a.type == self.hand_b.type

        assert self.hand_b > self.hand_a
        assert self.hand_d > self.hand_c


class TestTypes:
    def test_eq(self):
        assert Hand("33332").type == Hand("33332").type

    def test_lt(self):
        assert Hand("2AAAA").type < Hand("33322").type

    def test_gt(self):
        assert Hand("33322").type > Hand("2AAAA").type


def test_types():
    assert Hand("QJJQ2", jokers=True).type == Hand.Types.FOUR_OF_A_KIND
    assert Hand("JKKK2", jokers=True) > Hand("QQQQ2", jokers=True)

    assert Hand("AJAAA", jokers=True).type == Hand.Types.FIVE_OF_A_KIND


def test_one():
    hands = parse(test_input)
    assert one(hands) == 6440


def test_two():
    hands = parse(test_input, True)

    hands[0].type == Hand.Types.ONE_PAIR
    hands[1].type == Hand.Types.FOUR_OF_A_KIND
    hands[2].type == Hand.Types.TWO_PAIR
    hands[3].type == Hand.Types.FOUR_OF_A_KIND
    hands[4].type == Hand.Types.FOUR_OF_A_KIND

    assert one(hands) == 5905
