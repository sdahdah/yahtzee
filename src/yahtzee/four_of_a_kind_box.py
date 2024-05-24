"""Four of a kind scoring box."""

import numpy as np


def four_of_a_kind(dice: np.ndarray) -> int:
    """Add up the total of all the dice if there are four of a kind.

    If there are at least four dice rolled of the same number, then you can
    score the total sum of the dice in this box. If there are not at least four
    of the same number rolled, you may score 0 in this box.

    Parameters
    ----------
    dice : np.ndarray
        Array of die rolls.

    Returns
    -------
    int :
        Score.
    """

    for dice_val in range(1, 7):
        if dice[dice == dice_val].size == 4:
            return np.sum(dice)
    
    return 0
