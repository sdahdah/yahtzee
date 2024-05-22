"""Low straight scoring box."""

import numpy as np


def low_straight(dice: np.ndarray) -> int:
    """Four in a row gives a flat 30 points.

    A low straight is any sequence that runs through four numbers and is worth
    30 points. If you do not have a sequence that includes four consecutive
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
