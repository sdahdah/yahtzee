"""Test ``threes_box.py``."""

import numpy as np
import yahtzee.threes_box

def test_all_threes():
    """Test all threes array."""
    dice = np.array([3,3,3,3,3])
    score = yahtzee.threes_box.threes(dice)
    assert score == 15

def test_no_threes():
    """Test array w no threes."""
    dice = np.array([1,1,1,1,1])
    score = yahtzee.threes_box.threes(dice)
    assert score == 0
