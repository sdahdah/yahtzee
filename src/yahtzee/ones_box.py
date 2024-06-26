"""Ones scoring box."""

import numpy as np


def ones(dice: np.ndarray) -> int:
    """Add up the total of the ones and write the total into this box.

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
    for i in dice:
        if i == 1:
            score += 1
    return score
