"""Three of a kind scoring box."""

import numpy as np


def three_of_a_kind(dice: np.ndarray) -> int:
    """Add up the total of all the dice if there are three of a kind.

    If there are at least three dice rolled of the same number, then you can
    score the total sum of the dice in this box. If there are not at least
    three of the same number rolled, you may score 0 in this box.

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
