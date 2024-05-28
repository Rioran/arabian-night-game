import pytest

import source.game.deck as deck

new_deck = deck.Deck()

test_deck = [
     '2♠️', '3♠️', '4♠️', '5♠️', '6♠️', '7♠️', '8♠️', '9♠️', '10♠️', 'J♠️', 'Q♠️', 'K♠️', 'A♠️', '2♣️', '3♣️', '4♣️',
     '5♣️', '6♣️', '7♣️', '8♣️', '9♣️', '10♣️', 'J♣️', 'Q♣️', 'K♣️', 'A♣️', '2♦️', '3♦️', '4♦️', '5♦️', '6♦️', '7♦️',
     '8♦️', '9♦️', '10♦️', 'J♦️', 'Q♦️', 'K♦️', 'A♦️', '2♥️', '3♥️', '4♥️', "5♥️", "6♥️", '7♥️', '8♥️', '9♥️', '10♥️',
     'J♥️', 'Q♥️', 'K♥️', 'A♥️'
]



def test_generate_deck_cards():
    test_deck = new_deck._generate_deck_cards()
    assert_text = 'Check len deck'
    calculation = len(test_deck)
    desired_result = 52
    assert calculation == desired_result, assert_text


def test_get_cart():
    assert_text = 'Check random card'
    random_card_class = new_deck.get_card()
    calculation = random_card_class.name
    desired_result = test_deck
    assert calculation in desired_result, assert_text


