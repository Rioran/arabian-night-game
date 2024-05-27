from .deck import Deck
from .hand import Hand
from .utilities import ask_yes_or_no_question


class Game:
    def __init__(self):
        self._deck: Deck = Deck()
        self._games_played = 0
        self._player_victories = 0
        self._player_hand: Hand | None = None
        self._dealer_hand: Hand | None = None
        self._is_game_interrupted: bool = False

    def run(self):
        print(
            '=> Welcome to the Arabian Night Casino! <=\n'
            'Here we deal BlackJack where Ace is always 11 points.'
        )
        while self._does_player_want_to_play() and len(self._deck):
            self._play_single_game()

        print('Thanks for passing by! See ya!')

    @staticmethod
    def _does_player_want_to_play() -> bool:
        player_answer = ask_yes_or_no_question('Do you want to play?')
        return player_answer

    @staticmethod
    def _does_player_want_a_card() -> bool:
        player_answer = ask_yes_or_no_question('Do you want one more card?')
        return player_answer

    def _play_single_game(self):
        self._fill_dealer_hand()
        self._dealer_hand.show_cards_partially()

        self._fill_player_hand()

        if self._is_game_interrupted:
            print('Current game is aborted.')
            return

        self._player_hand.show_all_cards()
        self._games_played += 1

        self._decide_the_winner()
        print(f'You played {self._games_played} games and won {self._player_victories} times!')

    def _fill_dealer_hand(self):
        self._dealer_hand: Hand = Hand('Dealer')

        while (self._dealer_hand.value < 16) and len(self._deck):
            new_card = self._deck.get_card()
            self._dealer_hand.receive(new_card)

    def _fill_player_hand(self):
        self._player_hand: Hand = Hand('Player')

        while self._does_player_want_a_card():
            if not len(self._deck):
                print('Sorry, not enough cards to play...')
                self._is_game_interrupted = True
                return

            new_card = self._deck.get_card()
            self._player_hand.receive(new_card)
            self._player_hand.show_all_cards()

            if self._player_hand.value > 21:
                print('You took too much cards, sorry!')
                return

    def _decide_the_winner(self):
        player_value = self._player_hand.value
        print(f'Player has {player_value} points.')

        dealer_value = self._dealer_hand.value
        print(f'Dealer has {dealer_value} points.')

        if player_value > 21:
            print('Player has lost by taking too much cards!')
            return

        if dealer_value > 21:
            print('Dealer has lost by taking too much cards!')
            self._player_victories += 1
            return

        if dealer_value >= player_value:
            print('Dealer has won!')
            return

        print('Player has won!')
        self._player_victories += 1
