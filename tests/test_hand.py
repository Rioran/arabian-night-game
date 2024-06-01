import unittest
from unittest.mock import Mock
from source.game.hand import Hand
from source.game.card import Card

class TestHand(unittest.TestCase):

    def setUp(self):
        self.card_mock = Mock(spec=Card)
        self.card_mock.value = 10
        self.owner_name = "Player 1"
        self.hand = Hand(self.owner_name)

    def test__initial_state(self):
        self.assertEqual(self.hand.owner, self.owner_name)
        self.assertEqual(self.hand.cards, [])
        self.assertEqual(self.hand.value, 0)
        self.assertEqual(repr(self.hand), f'Player 1 has 0 cards.')

    def test__receive_card(self):
        self.hand.receive(self.card_mock)
        self.assertIn(self.card_mock, self.hand.cards)
        self.assertEqual(self.hand.value, self.card_mock.value)
        self.assertEqual(repr(self.hand), f'Player 1 has 1 cards.')

    def test__show_all_cards(self):
        with unittest.mock.patch('builtins.print') as mocked_print:
            self.hand.receive(self.card_mock)
            self.hand.show_all_cards()
            mocked_print.assert_called_with(f'10 points: {self.hand.cards}')

    def test__show_cards_partially(self):
        with unittest.mock.patch('builtins.print') as mocked_print:
            self.card_mock_2 = Mock(spec=Card)
            self.card_mock_2.value = 5
            self.hand.receive(self.card_mock)
            self.hand.receive(self.card_mock_2)
            self.hand.show_cards_partially()
            mocked_print.assert_called_with(
                f'Player 1 cards: 1 hidden and 1 others: {self.hand.cards[1:]}'
            )


if __name__ == '__main__':
    unittest.main()