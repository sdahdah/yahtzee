"""Test ``fives_box.py``."""

import numpy as np
import yahtzee.fives_box

def test_one_five():
    num = yahtzee.fives_box.fives(np.array([1,1,1,1,5]))
    assert num == 5

def test_no_five():
    num = yahtzee.fives_box.fives(np.array([1,1,1,1,1]))
    assert num == 0

def test_three_fives():
    num = yahtzee.fives_box.fives(np.array([1,1,5,5,5]))
    assert num == 15
