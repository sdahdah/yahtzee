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
    raise NotImplementedError()
