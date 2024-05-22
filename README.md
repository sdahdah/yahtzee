# Yahtzee: The Collaborative Git Exercise

[![Test package](https://github.com/sdahdah/yahtzee/actions/workflows/test-package.yml/badge.svg?branch=main)](https://github.com/sdahdah/yahtzee/actions/workflows/test-package.yml)

For this exercise, we will collaboratively build a tool for scoring Yahtzee
dice according to [these rules](https://yahtzee-rules.com/). The pedantic among
you will soon notice that we are not playing with bonuses, Jokers, or chance.
I'm truly sorry if that bothers you.

I have provided `play_yahtzee.py`, which rolls five dice, evaluates each score
box, and chooses the highest scoring one. The only problem is... none of the
scoring functions are implemented yet!

Each one of you will implement the empty function in one of

- `ones.py`,
- `twos.py`,
- `threes.py`,
- `fours.py`,
- `fives.py`,
- `sixes.py`,
- `three_of_a_kind.py`,
- `four_of_a_kind.py`,
- `full_house.py`,
- `low_straight.py`,
- `high_straight.py`, or
- `yahtzee.py`.

You will also be responsible for writing unit tests in the corresponding test
file in `tests/`. Each of you will submit a pull request to merge your changes
into the `main` branch, and each of you will review someone else's pull
request.

I have provided `test_play_yahtzee.py` which tests the full scoring
functionality, but will fail without your contributions. To run it, just type
run `play_yahtzee` in your terminal when the virtual environment is active.
Once everything is done, we should see the tests passing on GitHub!

Please install the `yahtzee` package in a new virtual environment on your
computer using `pip install -e ./yahtzee`. Be sure to also run `pip install -r
./requirements.txt` to install `pytest`.

To run the tests, run `pytest` in the root directory of the repo.

Now let's roll some dice...
