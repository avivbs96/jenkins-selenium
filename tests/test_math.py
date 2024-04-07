import pytest

def add_two_nums(a, b):
    return a + b

@pytest.mark.math
def test_small_nums():
    assert add_two_nums(1,2) == 3 , "The sum of 1+2 should be 3"


@pytest.mark.math
def test_large_nums():
    assert add_two_nums(100,300) == 400 , "The sum of 100 and 300 should be 400"