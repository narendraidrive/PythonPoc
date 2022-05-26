from unittest import mock
from unittest.mock import call
import pytest
from program_file.parametrize import guess_number 
from program_file.dice import roll_dice, random_sum
import pdb

@pytest.mark.parametrize("_input,expected", [(3, "You won!"), (4, "You lost!")])
@mock.patch("program_file.parametrize.roll_dice")

def test_guess_number(mock_roll_dice, _input, expected):
    mock_roll_dice.return_value = 3
    assert guess_number(_input) == expected
    mock_roll_dice.assert_called_once()

@mock.patch("program_file.dice.random.randint")
def test_random_sum(mock_randint):
    mock_randint.side_effect = [3, 4]
    assert random_sum() == 7
    mock_randint.assert_has_calls(calls=[call(1, 10), call(1, 7)])