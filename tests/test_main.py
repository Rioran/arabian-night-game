from time import sleep

from source.main import main
from source.game import Game
from .fixtures import mock_game


def test_main(mock_game):
    main()
    Game.__init__.assert_called_once()
    Game.run.assert_called_once()
