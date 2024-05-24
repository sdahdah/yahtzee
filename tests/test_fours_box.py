"""Test ``fours_box.py``."""

import numpy as np
import yahtzee.fours_box

def test_fours():
    """Test fours"""
    assert yahtzee.fours_box.fours(np.array([4, 1, 4, 2, 5])) == 8