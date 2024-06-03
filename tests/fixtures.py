import pytest
from unittest.mock import Mock

from source.game import Game


@pytest.fixture
def mock_game():
    initial_game_init = Game.__init__
    initial_game_run = Game.run
    Game.__init__ = Mock(return_value=None)
    Game.run = Mock()
    yield
    Game.__init__ = initial_game_init
    Game.run = initial_game_run
