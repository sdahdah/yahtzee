"""Sixes scoring box."""

import numpy as np


def sixes(dice: np.ndarray) -> int:
    """Add up the total of the sixes and write the total into this box.

    Parameters
    ----------
    dice : np.ndarray
        Array of die rolls.

    Returns
    -------
    int :
        Score.
    """
    # Where are there sixes?
    sixes = np.where(dice == 6, 1, 0,)

    # How many sixes are there?
    nb_sixes = np.sum(sixes)

    # What is the score?
    score = 6 * nb_sixes

    return score
