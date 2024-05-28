from source import main
import unittest
from unittest.mock import patch, MagicMock
from source.game.game import Game

def test__will_be_here__may_be():
    assert main is not None


class TestGame(unittest.TestCase):
    def setUp(self):
        self.game = Game()
        self.game._deck = MagicMock()
        self.game._play_single_game = MagicMock()

    @patch('builtins.print')
    @patch('builtins.input', return_value='n')
    def test_run_no_play(self, input_mock, print_mock):
        self.game.run()
        print_mock.assert_any_call('Thanks for passing by! See ya!')
        self.game._play_single_game.assert_not_called()

    @patch('builtins.print')
    @patch('builtins.input', side_effect=['y', 'n'])
    def test_run_play_once(self, input_mock, print_mock):
        self.game._deck.__len__.return_value = 1
        self.game.run()
        print_mock.assert_any_call('Thanks for passing by! See ya!')
        self.game._play_single_game.assert_called_once()

    @patch('builtins.print')
    @patch('builtins.input', side_effect=['y', 'y', 'n'])
    def test_run_play_twice(self, input_mock, print_mock):
        self.game._deck.__len__.return_value = 2
        self.game.run()
        print_mock.assert_any_call('Thanks for passing by! See ya!')
        self.assertEqual(self.game._play_single_game.call_count, 2)

    @patch('builtins.print')
    @patch('builtins.input', return_value='n')
    def test_does_player_want_to_play(self, input_mock, print_mock):
        self.assertEqual(self.game._does_player_want_to_play(), False)

    @patch('builtins.print')
    @patch('builtins.input', return_value='n')
    def test_does_player_want_a_card(self, input_mock, print_mock):
        self.assertEqual(self.game._does_player_want_a_card(), False)


if __name__ == '__main__':
    unittest.main()
