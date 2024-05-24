"""Test ``three_of_a_kind_box.py``."""

import numpy as np
import yahtzee.three_of_a_kind_box

def test_three_of_a_kind():
    """Test three of a kind."""
    dice = np.array([1, 2, 3, 4, 5])
    assert yahtzee.three_of_a_kind_box.three_of_a_kind(dice) == 0

    dice = np.array([1, 1, 1, 4, 5])
    assert yahtzee.three_of_a_kind_box.three_of_a_kind(dice) == 12

    dice = np.array([1, 1, 1, 1, 1])
    assert yahtzee.three_of_a_kind_box.three_of_a_kind(dice) == 5