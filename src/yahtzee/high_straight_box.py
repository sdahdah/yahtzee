"""High straight scoring box."""

import numpy as np


def high_straight(dice: np.ndarray) -> int:
    """Five in a row gives a flat 40 points.

    A high straight is any sequence that runs through five numbers and is worth
    40 points. If you do not have a sequence that includes five consecutive
    numbers, then score 0.

    Parameters
    ----------
    dice : np.ndarray
        Array of die rolls.

    Returns
    -------
    int :
        Score.
    """

    # Check if the dice array is valid
    if not isinstance(dice, np.ndarray):
        raise TypeError("dice must be a numpy array")
    


    if dice.size != 5:
        score = 0
    else:
        
        # Sort the dice array
        dice = np.sort(dice)
        # Check if the dice array is a high straight
        if np.array_equal(dice, np.array([2, 3, 4, 5, 6])):
            score = 40
        elif np.array_equal(dice, np.array([1, 2, 3, 4, 5])):
            score = 40
        else:
            score = 0

    return score