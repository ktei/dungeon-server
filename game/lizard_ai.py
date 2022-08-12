"""
Poor man's AI for lizard NPCs
This module does not have a real AI. Its purpose is
to produce some data to be passed to client side, so
we can test the communication between back and front.
"""
from random import randint
from time import time
from typing import Dict, List, Optional

from game.common_types import Direction


class LizardAI:
    """
    Implementation of lizard patrol AI
    """

    def __init__(self):
        self._lizard_states: Dict[int, Dict] = {}
        self._last_update_timestamps: Dict[int, Optional[time]] = {}

    def update_states(self, data: List):
        """
        Replace current states with new state
        """
        for item in [x for x in data if x["name"] == "lizard"]:
            self._lizard_states[item["id"]] = item

    def compute_directions(self) -> Dict[int, Direction]:
        """
        Based on current states, compute the future directions
        of the lizards
        """
        result: Dict[int, Direction] = {}
        for lizard_id, state in self._lizard_states.items():
            # update time threshold is random
            threshold = randint(1, 4)  # every 1-4 secs, we change direction
            should_update = state.get(
                "collision", None
            ) is not None or self.is_time_to_update(lizard_id, threshold)
            if should_update:
                # push the next direction into result
                result[lizard_id] = LizardAI.get_next_direction(state["direction"])
                self._last_update_timestamps[lizard_id] = time()
        return result

    def is_time_to_update(self, lizard_id: int, threshold: int) -> bool:
        """
        Given a lizard id, compute the time difference
        between last update and current time. If the difference
        is greater or equal than the threshold (seconds),
        return true, otherwise false
        """
        now = time()
        if lizard_id in self._last_update_timestamps:
            diff = int(now - self._last_update_timestamps.get(lizard_id))
            return diff >= threshold

        return True

    @staticmethod
    def get_next_direction(direction: Direction) -> Direction:
        """
        Given current direction, randomly return a direction
        that is NOT current direction
        """
        candidates = [Direction.UP, Direction.LEFT, Direction.DOWN, Direction.RIGHT]
        candidates.remove(direction)
        idx = randint(0, len(candidates) - 1)
        return candidates[idx]
