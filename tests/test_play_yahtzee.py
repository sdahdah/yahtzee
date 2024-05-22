"""Test ``play_yahtzee.py``."""

import numpy as np
import yahtzee


def test_fives():
    """Test fives."""
    name, score = yahtzee.score_dice(np.array([1, 3, 5, 5, 1]))
    assert name == "fives"
    assert score == 10


def test_four_of_a_kind():
    """Test four_of_a_kind."""
    name, score = yahtzee.score_dice(np.array([5, 5, 5, 5, 1]))
    assert name == "four_of_a_kind"
    assert score == 21


def test_fours():
    """Test fours."""
    name, score = yahtzee.score_dice(np.array([1, 3, 4, 4, 1]))
    assert name == "fours"
    assert score == 8


def test_full_house():
    """Test full_house."""
    name, score = yahtzee.score_dice(np.array([1, 1, 5, 5, 1]))
    assert name == "full_house"
    assert score == 25


def test_high_straight():
    """Test high_straight."""
    name, score = yahtzee.score_dice(np.array([1, 2, 3, 4, 5]))
    assert name == "high_straight"
    assert score == 40


def test_low_straight():
    """Test low_straight."""
    name, score = yahtzee.score_dice(np.array([1, 2, 3, 4, 1]))
    assert name == "low_straight"
    assert score == 30


def test_sixes():
    """Test sixes."""
    name, score = yahtzee.score_dice(np.array([1, 1, 2, 6, 6]))
    assert name == "sixes"
    assert score == 12


def test_three_of_a_kind():
    """Test three_of_a_kind."""
    name, score = yahtzee.score_dice(np.array([1, 3, 5, 5, 5]))
    assert name == "three_of_a_kind"
    assert score == 19


def test_threes():
    """Test threes."""
    name, score = yahtzee.score_dice(np.array([3, 3, 1, 2, 2]))
    assert name == "threes"
    assert score == 6


def test_twos():
    """Test twos."""
    name, score = yahtzee.score_dice(np.array([2, 2, 1, 1, 3]))
    assert name == "twos"
    assert score == 4


def test_yahtzee():
    """Test yahtzee."""
    name, score = yahtzee.score_dice(np.array([1, 1, 1, 1, 1]))
    assert name == "yahtzee"
    assert score == 50
