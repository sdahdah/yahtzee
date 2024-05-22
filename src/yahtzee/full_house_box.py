"""Full house scoring box."""

import numpy as np


def full_house(dice: np.ndarray) -> int:
    """Three of one kind and two of another gives a flat 25 points.

    A full house is where you have three of one number and two of another
    number. This scores 25 points. Otherwise score 0.

    Example: 1, 4, 3, 3, 3 = 0 points. 4, 1, 1, 4, 4 = 25 points.

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
