import random

import pytest

import source.game.deck as deck
from source.game.card import Card


def test_deck__create_instance():
    test_instance_deck = deck.Deck()

    assert test_instance_deck is not None
    assert test_instance_deck.cards is not None
    assert repr(test_instance_deck) == '<Deck: 52 cards>'
    assert len(test_instance_deck) == 52
    assert isinstance(test_instance_deck.cards[0], Card) is True


def test_deck__shuffle_cards():
    random.seed(1)
    first_instance_deck = deck.Deck()
    random.seed(2)
    second_instance_deck = deck.Deck()

    first_name_cards = [card.name for card in first_instance_deck.cards]
    second_name_cards = [card.name for card in second_instance_deck.cards]

    len_first_deck = len(first_instance_deck)
    len_second_deck = len(second_instance_deck)

    assert first_name_cards != second_name_cards
    assert len_first_deck == len_second_deck


@pytest.mark.parametrize(
    'card_name, desire_result',
    [
        ('2♠', 0),
        ('A♣', 25),
        ('A♥', 51),
    ]
)
def test_deck__generate_deck_cards__create_cards(card_name, desire_result):
    instance_deck = deck.Deck()
    test_cards = instance_deck._generate_deck_cards()
    name_cards = [card.name for card in test_cards]
    calculate_index = name_cards.index(card_name)
    assert isinstance(test_cards[calculate_index], Card) is True, f'{calculate_index} card is instance of Card'
    assert calculate_index == desire_result, f'{calculate_index} card with name {card_name} has position {calculate_index}'


def test_deck__positive_get_card():
    test_instance_deck = deck.Deck()
    full_name_cards = [card.name for card in test_instance_deck.cards]
    random_card = test_instance_deck.get_card()
    name_cards_without_random_card = [card.name for card in test_instance_deck.cards]
    calculation = random_card.name
    assert calculation in full_name_cards
    assert calculation == full_name_cards[-1]
    assert calculation not in name_cards_without_random_card


def test_deck__negative_get_card():
    test_instance_deck = deck.Deck()
    test_instance_deck.cards = []
    with pytest.raises(deck.OutOfCardsError):
        test_instance_deck.get_card()


def test_deck__length_deck():
    assert_text = 'Check len function for the deck'
    test_deck = deck.Deck()
    calculation = len(test_deck)
    desired_result = 52
    assert calculation == desired_result, assert_text


def test_deck__repr():
    test_instance_deck = deck.Deck()
    repr_string = repr(test_instance_deck)
    desired_result = '<Deck: 52 cards>'
    assert repr_string == desired_result
