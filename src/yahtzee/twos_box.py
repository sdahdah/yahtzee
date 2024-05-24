"""Twos scoring box."""

import numpy as np


def twos(dice: np.ndarray) -> int:
    """Add up the total of the twos and write the total into this box.

    Parameters
    ----------
    dice : np.ndarray
        Array of die rolls.

    Returns
    -------
    int :
        Score.
    """
    count=0
    for value in dice:
        if value == 2:
            count=count+1
    
    return 2*count


    raise NotImplementedError()
