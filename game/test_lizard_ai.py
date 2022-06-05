from game.common_types import Coordinate, Direction
from game.lizard_ai import LizardAI, State


def test_compute_directions():
    """
    Test if SUT can return directions different from
    the current directions per lizard
    """

    sut = LizardAI()
    sut.update_states(
        {
            1: State(Coordinate(100, 200), Direction.NONE, False),
            2: State(Coordinate(300, 400), Direction.RIGHT, False),
        }
    )

    actual = sut.compute_directions()

    assert actual[1] != Direction.NONE
    assert actual[2] != Direction.RIGHT
