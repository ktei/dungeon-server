"""
A collection of commonly shared types
"""
from collections import namedtuple
from enum import IntEnum
from typing import NamedTuple

Coordinate = namedtuple("Coordinate", "x y")


class Direction(IntEnum):
    """
    The 4 directions a character or NPC can face to
    """

    NONE = -1
    UP = 0
    RIGHT = 1
    DOWN = 2
    LEFT = 3


class State(NamedTuple):
    """
    The class to describe a game object's state in the game,
    such as its coordinate, direction etc.
    """

    coord: Coordinate
    direction: Direction
    is_collided: bool  # wether lizard has collided with wall
