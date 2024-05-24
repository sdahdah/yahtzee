"""Threes scoring box."""

import numpy as np


def threes(dice: np.ndarray) -> int:
    """Add up the total of the threes and write the total into this box.

    Parameters
    ----------
    dice : np.ndarray
        Array of die rolls.

    Returns
    -------
    int :
        Score.
    """
    score = 0
    for i in range(len(dice)):
        if dice[i] == 3:
            score += 3

    return score