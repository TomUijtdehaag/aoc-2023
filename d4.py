from pydantic import BaseModel

from utils.read import readlines


class Card(BaseModel):
    card: int
    winning_numbers: list[int]
    your_numbers: list[int]

    def value(self):
        v = 0
        for n in self.your_numbers:
            if n in self.winning_numbers and v == 0:
                v += 1

            elif n in self.winning_numbers and v > 0:
                v *= 2

        return v

    def amount(self):
        v = 0
        for n in self.your_numbers:
            if n in self.winning_numbers:
                v += 1

        return v


def parse(card: str):
    card, numbers = card.split(":")
    card = int(card.split()[-1])
    winning_numbers, your_numbers = numbers.split("|")
    winning_numbers = [int(n) for n in winning_numbers.strip().split()]
    your_numbers = [int(n) for n in your_numbers.strip().split()]

    return Card(card=card, winning_numbers=winning_numbers, your_numbers=your_numbers)


def one(cards: list[Card]):
    return sum([card.value() for card in cards])


def copies(cards: list[Card]):
    copies = {card.card: 1 for card in cards}

    for card in cards:
        for i in range(1, card.amount() + 1):
            try:
                copies[card.card + i] += copies[card.card]

            except KeyError:
                continue

    return copies


def two(cards: list[Card]):
    card_copies = copies(cards)
    return sum(card_copies.values())


if __name__ == "__main__":
    lines = readlines("input/4.txt")
    cards = [parse(line) for line in lines]

    print("Part one:", one(cards))
    print("Part two:", two(cards))
