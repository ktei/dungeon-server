"""
A collection of commonly shared types
"""
from collections import namedtuple
from enum import IntEnum

Coordinate = namedtuple("Coordinate", "x y")


class Direction(IntEnum):
    """
    The 4 directions a character or NPC can face to
    """

    UP = 0
    RIGHT = 1
    DOWN = 2
    LEFT = 3

