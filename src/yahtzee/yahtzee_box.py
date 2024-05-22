"""Yahtzee scoring box."""

import numpy as np


def yahtzee(dice: np.ndarray) -> int:
    """Five identical numbers gives 50 flat points.

    A yahtzee is where all five dice are the same and is worth 50 points! If
    you do not have five numbers the same, then score 0.

    Parameters
    ----------
    dice : np.ndarray
        Array of die rolls.

    Returns
    -------
    int :
        Score.
    """
    raise NotImplementedError()
