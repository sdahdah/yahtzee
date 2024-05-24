"""Test ``yahtzee_box.py``."""

import numpy as np
import yahtzee.yahtzee_box

def test_yahtzee():
    dice_roll_cases = [
        [1,1,1,1,1],
        [0,2,1,1,1],
        [4,4,4,4,4]
        [2,2,2,2,6]
    ]
    expected_results = [50,0,50,0]
    for k, dice_roll in enumerate(dice_roll_cases):
        result = yahtzee.yahtzee_box(np.array(dice_roll))
        assert(result == expected_results[k])