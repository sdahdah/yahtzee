"""Test ``sixes_box.py``."""

import numpy as np
import yahtzee.sixes_box

def test_no_sixes():
    roll = np.array([1, 1, 1, 1, 1])
    sixes = yahtzee.sixes_box.sixes(roll)
    assert sixes == 0

def test_one_six():
    roll = np.array([1, 2, 6, 4, 4])
    sixes = yahtzee.sixes_box.sixes(roll)
    assert sixes == 6

def test_two_sixes():
    roll = np.array([6, 1, 6, 2, 5])
    sixes = yahtzee.sixes_box.sixes(roll)
    assert sixes == 12

def test_three_sixes():
    roll = np.array([6, 2, 2, 6, 6])
    sixes = yahtzee.sixes_box.sixes(roll)
    assert sixes == 18

def test_four_sixes():
    roll = np.array([6, 6, 6, 6, 3])
    sixes = yahtzee.sixes_box.sixes(roll)
    assert sixes == 24

def test_five_sixes():
    roll = np.array([6, 6, 6, 6, 6])
    sixes = yahtzee.sixes_box.sixes(roll)
    assert sixes == 30

