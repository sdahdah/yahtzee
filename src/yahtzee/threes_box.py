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
    for d in dice:
        if d == 3:
            score += 3
    
    return score