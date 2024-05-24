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

    score_1 = np.array([1, 2, 3, 4])
    score_2 = np.array([2, 3, 4, 5])
    score_3 = np.array([3, 4, 5, 6])
    all_scores = [score_1, score_2, score_3]

    for score in all_scores:
        if np.all(np.isin(score, dice)):
            return 30
        
    return 0 
