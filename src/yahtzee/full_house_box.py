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
    count = np.zeros(6,)
    '''
    count[0] = (dice == 1).sum()
    count[1] = (dice == 2).sum()
    count[2] = (dice == 3).sum()
    count[3] = (dice == 4).sum()
    count[4] = (dice == 5).sum()
    count[5] = (dice == 6).sum()
    '''
    
    for i in range(count.size):
        count[i] = (dice == i + 1).sum()
        

    if (3 in count) and (2 in count):
        score = 25
    else:
        score = 0


    # raise NotImplementedError()
    return score
