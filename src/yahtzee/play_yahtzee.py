"""Play a game of Yahtzee."""

from typing import Tuple

import numpy as np

from .fives_box import fives
from .four_of_a_kind_box import four_of_a_kind
from .fours_box import fours
from .full_house_box import full_house
from .high_straight_box import high_straight
from .low_straight_box import low_straight
from .ones_box import ones
from .sixes_box import sixes
from .three_of_a_kind_box import three_of_a_kind
from .threes_box import threes
from .twos_box import twos
from .yahtzee_box import yahtzee


def play_yahtzee():
    """Play a game of Yahtzee with a random die roll."""
    rng = np.random.default_rng()
    roll = rng.integers(low=1, high=6, size=5)
    print(f" Roll: {roll}")
    name, score = score_dice(roll)
    print(f"Score: {score}, {name}")


def score_dice(dice: np.ndarray) -> Tuple[str, int]:
    """Score every scoring block and pick the highest.

    Parameters
    ----------
    dice : np.ndarray
        Array of die rolls.

    Returns
    -------
    Tuple[str, int] :
        Name of scoring box and score.
    """
    scoring_boxes = [
        fives,
        four_of_a_kind,
        fours,
        full_house,
        high_straight,
        low_straight,
        ones,
        sixes,
        three_of_a_kind,
        threes,
        twos,
        yahtzee,
    ]
    scores = np.array([scoring_box(dice) for scoring_box in scoring_boxes])
    max_score = np.max(scores)
    # If you find yourself needing to use ``__name__``, you are probably doing
    # something sketchy... Do as I say, not as I do.
    name = scoring_boxes[np.argmax(scores)].__name__
    return name, max_score
