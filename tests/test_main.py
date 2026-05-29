# test_max_repeating_element.py
import pytest
from max_repeating_element import find_max_repeating_element

def test_empty_list():
    assert find_max_repeating_element([]) is None

def test_single_element_list():
    assert find_max_repeating_element([1]) == 1

def test_list_with_two_elements():
    assert find_max_repeating_element([1, 1]) == 1

def test_list_with_three_elements():
    assert find_max_repeating_element([1, 2, 2]) == 2

def test_list_with_multiple_repeating_elements():
    assert find_max_repeating_element([1, 2, 2, 3, 3, 3]) == 3

def test_list_with_negative_numbers():
    assert find_max_repeating_element([-1, -1, -2, -2]) == -1

def test_list_with_zero():
    assert find_max_repeating_element([0, 0, 0]) == 0
