import enum
from dataclasses import dataclass

from utils.read import readlines


@dataclass
class Card:
    CARDS = {
        v: r for r, v in enumerate("A, K, Q, J, T, 9, 8, 7, 6, 5, 4, 3, 2".split(", "))
    }
    CARDS_JOKERS = {
        v: r for r, v in enumerate("A, K, Q, T, 9, 8, 7, 6, 5, 4, 3, 2, J".split(", "))
    }

    def __init__(self, value: str, jokers: bool = False):
        self.jokers = jokers
        self.value = value
        self.rank = self.get_rank()

    def get_rank(self):
        if self.jokers:
            return Card.CARDS_JOKERS[self.value]
        else:
            return Card.CARDS[self.value]

    def __hash__(self) -> int:
        return hash(self.value)

    def __eq__(self, other) -> bool:
        return self.value == other.value

    def __lt__(self, other) -> bool:
        return self.rank < other.rank

    def __gt__(self, other) -> bool:
        return self.rank > other.rank

    def __repr__(self) -> str:
        return f"{self.value}"


class Hand:
    def __init__(self, cards: str, bid: int = 0, jokers: bool = False):
        self.jokers = jokers
        self.cards = self.parse(cards)
        self.bid = bid
        self.type = self.get_type()

    class Types(enum.Enum):
        FIVE_OF_A_KIND = 0
        FOUR_OF_A_KIND = 1
        FULL_HOUSE = 2
        THREE_OF_A_KIND = 3
        TWO_PAIR = 4
        ONE_PAIR = 5
        HIGH_CARD = 6

        def __eq__(self, other):
            return self.value == other.value

        def __lt__(self, other):
            return self.value < other.value

        def __gt__(self, other):
            return self.value > other.value

    def parse(self, cards: str):
        return [Card(c, self.jokers) for c in cards]

    def get_type(self):
        counts = self.hand_count()

        first = counts[0]

        if first[1] == 5:
            return self.Types.FIVE_OF_A_KIND
        elif first[1] == 4:
            return self.Types.FOUR_OF_A_KIND
        elif first[1] == 3 and counts[1][1] == 2:
            return self.Types.FULL_HOUSE
        elif first[1] == 3:
            return self.Types.THREE_OF_A_KIND
        elif first[1] == 2 and counts[1][1] == 2:
            return self.Types.TWO_PAIR
        elif first[1] == 2:
            return self.Types.ONE_PAIR
        else:
            return self.Types.HIGH_CARD

    def hand_count(self) -> list[tuple[Card, int]]:
        counts = {}
        for card in self.cards:
            counts[card] = counts.get(card, 0) + 1

        if self.jokers:
            jokers = counts.pop(Card("J"), 0)
            if len(counts) == 0:
                return [(Card("J"), jokers)]

            most_common = max(counts, key=counts.get)
            counts[most_common] += jokers

        return sorted(counts.items(), key=lambda x: x[1], reverse=True)

    def __eq__(self, other):
        return self.cards == other.cards and self.bid == other.bid

    def __lt__(self, other):
        if self.type == other.type:
            return self.cards < other.cards

        else:
            return self.type < other.type

    def __gt__(self, other):
        if self.type == other.type:
            return self.cards > other.cards
        else:
            return self.type > other.type

    def __repr__(self):
        return f"{self.cards} ({self.type})"


def parse(input: list[str], jokers=False):
    hands = []
    for line in input:
        cards, bid = line.split()
        hands.append(Hand(cards, int(bid), jokers))

    return hands


def one(hands: list[Hand]):
    hands = sorted(hands, reverse=True)
    ranks = range(1, len(hands) + 1)

    return sum(h.bid * r for h, r in zip(hands, ranks))


if __name__ == "__main__":
    lines = readlines("input/7.txt")
    hands = parse(lines)

    print("Part one:", one(hands))

    hands = parse(lines, jokers=True)
    print("Part two:", one(hands))
