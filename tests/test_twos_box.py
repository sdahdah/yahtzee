"""Test ``twos_box.py``."""

import numpy as np
import yahtzee.twos_box

def test_no_twos():
    roll=np.array([1,3,4,5,6])
    value=yahtzee.twos_box.twos(roll)
    assert value == 0

def test_twos():
    roll=np.array([2,3,4,2,5])
    value=yahtzee.twos_box.twos(roll)
    assert value == 4

def test_all_twos():
    roll=np.array([2,2,2,2,2])
    value=yahtzee.twos_box.twos(roll)
    assert value == 10


