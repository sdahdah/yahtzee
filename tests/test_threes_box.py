"""Test ``threes_box.py``."""

import numpy as np
import yahtzee.threes_box

def test_threes():
    """Test threes."""
    dice = np.array([3,3,3,3,3])
    score = yahtzee.threes_box.threes(dice)
    assert score == 15
