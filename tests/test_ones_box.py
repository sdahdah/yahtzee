"""Test ``ones_box.py``."""

import numpy as np
import yahtzee.ones_box

def test_ones():
    """Test ones."""
    score = yahtzee.ones_box.ones(np.array([1, 3, 5, 5, 1]))
    assert score == 2