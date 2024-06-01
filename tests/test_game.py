from source import main
from source.game.game import Game
import unittest
from unittest.mock import patch, MagicMock

WELCOME_MESSAGE = '=> Welcome to the Arabian Night Casino! <=\nHere we deal BlackJack where Ace is always 11 points.'
GOODBYE_MESSAGE = 'Thanks for passing by! See ya!'
class TestGame(unittest.TestCase):
    def setUp(self):
        self.game = Game()
        self.game._deck = MagicMock()
        self.game._play_single_game = MagicMock()

    @patch('builtins.print')
    @patch('builtins.input', return_value='n')
    def test_run_no_play(self, input_mock, print_mock):
        self.game.run()
        print_mock.assert_any_call(WELCOME_MESSAGE)
        print_mock.assert_any_call(GOODBYE_MESSAGE)
        self.game._play_single_game.assert_not_called()

    @patch('builtins.print')
    @patch('builtins.input', side_effect=['y', 'n'])
    def test_run_play_once(self, input_mock, print_mock):
        self.game._deck.__len__.return_value = 1
        self.game.run()
        print_mock.assert_any_call(WELCOME_MESSAGE)
        print_mock.assert_any_call(GOODBYE_MESSAGE)
        self.game._play_single_game.assert_called_once()

    @patch('builtins.print')
    @patch('builtins.input', side_effect=['y', 'y', 'n'])
    def test_run_play_twice(self, input_mock, print_mock):
        self.game._deck.__len__.return_value = 2
        self.game.run()
        print_mock.assert_any_call(WELCOME_MESSAGE)
        print_mock.assert_any_call(GOODBYE_MESSAGE)
        self.assertEqual(self.game._play_single_game.call_count, 2)

    @patch('builtins.print')
    @patch('builtins.input', return_value='n')
    def test_does_player_want_to_play_no(self, input_mock, print_mock):
        self.assertEqual(self.game._does_player_want_to_play(), False)

    @patch('builtins.print')
    @patch('builtins.input', return_value='y')
    def test_does_player_want_to_play_yes(self, input_mock, print_mock):
        self.assertEqual(self.game._does_player_want_to_play(), True)

    @patch('builtins.print')
    @patch('builtins.input', return_value='n')
    def test_does_player_want_a_card_no(self, input_mock, print_mock):
        self.assertEqual(self.game._does_player_want_a_card(), False)

    @patch('builtins.print')
    @patch('builtins.input', return_value='y')
    def test_does_player_want_a_card_yes(self, input_mock, print_mock):
        self.assertEqual(self.game._does_player_want_a_card(), True)


if __name__ == '__main__':
    unittest.main()
