from .constants import RANKS_TO_VALUES


class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
        self.name = f'{rank}{suit}'
        self.value = RANKS_TO_VALUES[rank]

    def __repr__(self):
        return self.name
