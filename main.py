"""
Application entry point
"""

from typing import Dict

from flask import Flask
from flask_socketio import SocketIO

from game.server import GameServer

app = Flask(__name__)
app.config["SECRET_KEY"] = "secret!"
socketio = SocketIO(
    app,
    cors_allowed_origins=["http://localhost:3000"],
    engineio_logger=True,
    logger=True,
)

game_server = GameServer(socketio)


@socketio.on("data")
def handle_data(data: Dict[str, Dict]):
    game_server.receive_game_data(data)


if __name__ == "__main__":
    socketio.run(app)
