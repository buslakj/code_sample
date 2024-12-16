import pytest
from sample_3.sample_3 import triangleArea, points_Belong, side_length_helper

def test_is_not_nondegenerate():
    result = points_Belong(1, 1, 1, 2, 1, 3, 2, 2, 3, 3)
    assert result == 0

def test_all_the_same_point():
    result = points_Belong(1, 1, 1, 1, 1, 1, 1, 1, 1, 1)
    assert result == 0
    
def test_point_p_in_triangle():
    result = points_Belong(1, 1, 2, 3, 4, 2, 2, 2, 4, 4)
    assert result == 1

def test_point_q_in_triangle():
    result = points_Belong(1, 1, 2, 3, 4, 2, 1, 3, 3, 2)
    assert result == 2

def test_no_points_in_triangle():
    result = points_Belong(1, 1, 2, 3, 4, 2, 1, 3, 3, 6)
    assert result == 4

def test_both_points_in_triangle():
    result = points_Belong(1, 1, 2, 3, 4, 2, 2, 2, 3, 2)
    assert result == 3

def test_area_is_zero():
    area = triangleArea(1, 1, 1, 1, 1, 1)
    assert area == 0

def test_area_is_some():
    area = triangleArea(1, 1, 2, 3, 4, 2)

    assert round(area, 1) == 2.5

def test_side_length_zero():
    side_length = side_length_helper(1, 1, 1, 1)

    assert side_length == 0 

def test_side_length_some():
    side_length = side_length_helper(1, 1, 2, 3)

    assert round(side_length, 3) == 2.236