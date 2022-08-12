from typing import List

from flask_socketio import SocketIO

from game.lizard_ai import LizardAI


class GameServer:
    """
    The class which contains the high-level logic of the
    dungeon game server
    """

    def __init__(self, socket: SocketIO) -> None:
        self._lizard_ai = LizardAI()
        self._socket = socket

    def receive_game_data(self, data: List) -> None:
        self._lizard_ai.update_states(data)
        result = self._lizard_ai.compute_directions()
        self._socket.emit("data", result)
