"""Test ``fours_box.py``."""

import numpy as np
import yahtzee.fours_box

def test_fours():
    """Test fours"""
    name, score = yahtzee.score_dice(np.array([4, 1, 4, 2, 5]))
    assert name == "Fours" and score == 8