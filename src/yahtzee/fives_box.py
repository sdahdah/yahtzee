"""Fives scoring box."""

import numpy as np


def fives(dice: np.ndarray) -> int:
    """Add up the total of the fives and write the total into this box.

    Parameters
    ----------
    dice : np.ndarray
        Array of die rolls.

    Returns
    -------
    int :
        Score.
    """
    num_fives = 0
    for i in range(len(dice)):
        if dice[i] == 5:
            num_fives +=1
    return num_fives
