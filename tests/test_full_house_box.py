"""Test ``full_house_box.py``."""

import numpy as np
import yahtzee.full_house_box

def test_full_house_false():
    assert yahtzee.full_house_box.full_house(np.array([1, 1, 1, 2, 3])) == 0
    assert yahtzee.full_house_box.full_house(np.array([1, 4, 3, 3, 3])) == 0



def test_full_house_true():
    assert yahtzee.full_house_box.full_house(np.array([4, 1, 1, 4, 4])) == 25
    assert yahtzee.full_house_box.full_house(np.array([3, 3, 3, 2, 2])) == 25
