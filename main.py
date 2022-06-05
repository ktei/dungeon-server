"""
Application entry point
"""

from flask import Flask
from flask_socketio import SocketIO

from game.server import Server

app = Flask(__name__)
app.config["SECRET_KEY"] = "secret!"
socketio = SocketIO(
    app,
    cors_allowed_origins=["http://localhost:3000"],
    engineio_logger=True,
    logger=True,
)

server = Server(socketio)


@socketio.on("message")
def handle_message(data):
    server.receive_game_data(data)


if __name__ == "__main__":
    socketio.run(app)
