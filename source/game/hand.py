from .card import Card


class Hand:
    def __init__(self, owner_name: str):
        self.cards: list[Card] = list()
        self.value = 0
        self.owner = owner_name

    def __repr__(self):
        return f'{self.owner} has {len(self.cards)} cards.'

    def receive(self, card: Card):
        self.cards.append(card)
        self.value += card.value
        print(self)

    def show_all_cards(self):
        text = f'{self.value} points: {self.cards}'
        print(text)

    def show_cards_partially(self):
        other_cards = self.cards[1:]
        text = f'{self.owner} cards: 1 hidden and {len(other_cards)} others: {other_cards}'
        print(text)
