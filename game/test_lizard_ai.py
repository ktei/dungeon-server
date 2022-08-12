from game.common_types import Direction
from game.lizard_ai import LizardAI


def test_compute_directions():
    """
    Test if SUT can return directions different from
    the current directions per lizard
    """

    sut = LizardAI()
    sut.update_states(
        [
            {
                "id": 1,
                "name": "lizard",
                "x": 100,
                "y": 200,
                "direction": Direction.LEFT,
            },
            {
                "id": 2,
                "name": "lizard",
                "x": 300,
                "y": 400,
                "direction": Direction.RIGHT,
            },
            {"id": 3, "name": "hero", "x": 400, "y": 500, "direction": Direction.RIGHT},
        ]
    )

    actual = sut.compute_directions()

    assert actual[1] != Direction.LEFT
    assert actual[2] != Direction.RIGHT
    assert 3 not in actual
