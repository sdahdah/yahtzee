"""Test ``four_of_a_kind_box.py``."""

import numpy as np
import yahtzee.four_of_a_kind_box

def test_four_of_a_kind_success():
    score = yahtzee.four_of_a_kind_box.four_of_a_kind(np.array([4, 4, 4, 4, 1]))
    assert score == 17


    score = yahtzee.four_of_a_kind_box.four_of_a_kind(np.array([3, 4, 5, 1, 3]))
    assert score == 0
