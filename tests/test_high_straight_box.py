"""Test ``high_straight_box.py``."""

import numpy as np
import yahtzee.high_straight_box

def test_high_straight_box():
    score = yahtzee.high_straight_box.high_straight(np.array([1, 2, 3, 4, 5]))
    assert score == 40