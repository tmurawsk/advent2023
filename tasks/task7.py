from tasks.base import Task


CARDS_WEIGHT = {
    '2': 0, '3': 1, '4': 2, '5': 3, '6': 4, '7': 5, '8': 6,
    '9': 7, 'T': 8, 'J': 9, 'Q': 10, 'K': 11, 'A': 12
}

CARDS_WEIGHT2 = {
    '2': 0, '3': 1, '4': 2, '5': 3, '6': 4, '7': 5, '8': 6,
    '9': 7, 'T': 8, 'J': -1, 'Q': 10, 'K': 11, 'A': 12
}


def calc_cards(cards) -> dict:
    cards_count = {}
    for c in cards:
        if c not in cards_count:
            cards_count[c] = 0
        cards_count[c] += 1
    return cards_count


def calc_rank(cards) -> int:
    cards_count = calc_cards(cards)

    if len(cards_count) == 1:
        return 6    # 5 of a kid
    if len(cards_count) == 2:
        if max(cards_count.values()) == 4:
            return 5    # 4 of a kind
        return 4    # full house
    if len(cards_count) == 3:
        if max(cards_count.values()) == 3:
            return 3    # 3 of a kind
        return 2    # two pairs
    if len(cards_count) == 4:
        return 1    # one pair
    return 0    # high card


def calc_rank_jokers(cards) -> int:
    cards_count = calc_cards(cards)
    if 'J' not in cards_count:
        return calc_rank(cards)
    jokers = cards_count.pop('J')
    different_cards = len(cards_count.keys())
    max_different_cards = 0 if len(cards_count) == 0 else max(cards_count.values())

    if different_cards <= 1:
        return 6    # 5 of a kind
    if jokers == 3:
        return 5    # 4 of a kind
    if jokers == 2:
        if different_cards == 2:
            return 5    # 4 of a kind
        return 3    # 3 of a kind
    if different_cards == 2:
        if max_different_cards == 3:
            return 5    # 4 of a kind
        if max_different_cards == 2:
            return 4    # full house
    if different_cards == 3:
        return 3    # 3 of a kind
    return 1


class Hand:
    def __init__(self, cards: str, bid: int, first_task: bool = True):
        self.cards: str = cards
        self.bid: int = bid
        self.init_rank: int = calc_rank(self.cards) if first_task else calc_rank_jokers(self.cards)
        self.first_task = first_task

    def __eq__(self, other: "Hand"):
        return self.init_rank == other.init_rank and self.cards == other.cards

    def __gt__(self, other: "Hand"):
        weight = CARDS_WEIGHT if self.first_task else CARDS_WEIGHT2
        if self.init_rank != other.init_rank:
            return self.init_rank > other.init_rank
        for i in range(len(self.cards)):
            if not weight[self.cards[i]] == weight[other.cards[i]]:
                return weight[self.cards[i]] > weight[other.cards[i]]
        return False

    def __ne__(self, other):
        return not self.__eq__(other)

    def __lt__(self, other):
        return not self.__gt__(other) and self.__ne__(other)

    def __ge__(self, other):
        return not self.__lt__(other)

    def __le__(self, other):
        return not self.__gt__(other)


class Task7(Task):
    def __init__(self, filename="input/7.txt"):
        super().__init__(filename)

    def run1(self):
        hands: [Hand] = []
        for line in self.file:
            [cards, bid] = line.strip().split()
            hands.append(Hand(cards, int(bid)))
        hands.sort()

        result = 0
        for i in range(len(hands)):
            result += (i + 1) * hands[i].bid
        print(result)

    def run2(self):
        hands: [Hand] = []
        for line in self.file:
            [cards, bid] = line.strip().split()
            hands.append(Hand(cards, int(bid), False))
        hands.sort()

        result = 0
        for i in range(len(hands)):
            result += (i + 1) * hands[i].bid
        print(result)
