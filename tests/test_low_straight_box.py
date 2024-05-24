"""Test ``low_straight_box.py``."""

import numpy as np
import yahtzee.low_straight_box

def test_low_straight():
    '''Test low straight.'''
    score = yahtzee.low_straight_box.low_straight(np.array([1, 2, 3, 4, 5]))
    assert score == 30 