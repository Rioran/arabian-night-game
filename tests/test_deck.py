import pytest

import source.game.deck as deck


Deck = deck.Deck()
test_name_cards = [card.name for card in Deck.cards]


card_0 = '2♠'
card_25 = 'A♣'
card_51 = 'A♥'


def test_deck__create_instance():
    instance_deck = deck.Deck()

    assert instance_deck is not None
    assert instance_deck.cards is not None


def test_deck__shuffle_cards():
    first_instance_deck = deck.Deck()
    second_instance_deck = deck.Deck()

    first_name_cards = [card.name for card in first_instance_deck.cards]
    second_name_cards = [card.name for card in second_instance_deck.cards]

    len_first_deck = len(first_instance_deck)
    len_second_deck = len(second_instance_deck)

    assert first_name_cards != second_name_cards
    assert len_first_deck == len_second_deck


def test_deck__length_deck():
    assert_text = 'Check len function for the deck'
    new_deck = Deck._generate_deck_cards()
    calculation = len(new_deck)
    desired_result = 52
    assert calculation == desired_result, assert_text


def test_deck__generate_deck_cards():
    assert_text = 'Check _generate_deck_cards method'
    new_deck = Deck._generate_deck_cards()
    assert card_0 == new_deck[0].name, f'{assert_text}: generate first card {card_0}'
    assert card_25 == new_deck[25].name, f'{assert_text}: generate middle card {card_25}'
    assert card_51 == new_deck[51].name, f'{assert_text}: generate last card {card_51}'


def test_deck__positive_get_card():
    test_deck = deck.Deck()
    full_name_cards = [card.name for card in test_deck.cards]

    random_card = test_deck.get_card()

    name_cards_without_random_card = [card.name for card in test_deck.cards]

    calculation = random_card.name
    assert calculation in full_name_cards
    assert calculation == full_name_cards[-1]
    assert calculation not in name_cards_without_random_card


def test_deck__negative_get_card():
    test_deck = deck.Deck()
    with pytest.raises(deck.OutOfCardsError):
        for _ in range(53):
            test_deck.get_card()


def test_deck__repr():
    test_deck = deck.Deck()
    repr_string = repr(test_deck)
    desired_result = '<Deck: 52 cards>'
    assert repr_string == desired_result
