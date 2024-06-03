from random import shuffle

from .card import Card
from .constants import RANKS_TO_VALUES, SUITS


class OutOfCardsError(ValueError):
    pass


class Deck:
    def __init__(self):
        self.cards: list[Card] = self._generate_deck_cards()
        shuffle(self.cards)

    @staticmethod
    def _generate_deck_cards() -> list[Card]:
        """Generate a list with 52 cards. Unshuffled.

        >>> deck = Deck._generate_deck_cards()
        >>> len(deck)
        52
        >>> isinstance(Deck._generate_deck_cards()[0], Card)
        True
        """
        result: list[Card] = list()

        for suit in SUITS:
            for rank in RANKS_TO_VALUES.keys():
                card = Card(rank, suit)
                result.append(card)

        return result

    def get_card(self) -> Card:
        if self.cards:
            card = self.cards.pop()
            return card
        raise OutOfCardsError('Deck has no more cards.')

    def __len__(self):
        return len(self.cards)

    def __repr__(self):
        return f'<Deck: {len(self)} cards>'
