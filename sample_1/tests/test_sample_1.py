import pytest
from sample_1.sample import digit_count



def test_check_perfect_case():
    result = digit_count("1210")

    assert result == True

def test_false_case():
    result = digit_count("030")

    assert result == False

def test_is_str():
    result = digit_count(12)

    assert "Input type incorrect"