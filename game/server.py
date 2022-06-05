from json import dumps
from typing import Dict

from flask_socketio import SocketIO

from game.lizard_ai import LizardAI


class Server:
    """
    The class which contains the high-level logic of the
    dungeon game server
    """

    def __init__(self, socket: SocketIO) -> None:
        self._lizard_ai = LizardAI()
        self._socket = socket

    def receive_game_data(self, data: Dict[int, Dict]) -> None:
        self._lizard_ai.update_states(data)
        result = self._lizard_ai.compute_directions()
        print(dumps(result))
