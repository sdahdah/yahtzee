"""Fours scoring box."""

import numpy as np


def fours(dice: np.ndarray) -> int:
    """Add up the total of the fours and write the total into this box.

    Parameters
    ----------
    dice : np.ndarray
        Array of die rolls.

    Returns
    -------
    int :
        Score.
    """
    raise np.sum(dice[dice == 4])
