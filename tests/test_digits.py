#!/usr/bin/env python

"""Tests for `readyregex` package."""

import pytest

from readyregex import Digits, ReadyRegexException

@pytest.fixture
def no_digits():
    return Digits(0)

@pytest.fixture
def one_digit():
    return Digits(1)

@pytest.fixture
def two_digits():
    return Digits(2)

def test_no_digits(no_digits):
    assert no_digits.match_whole_string("")
    assert not no_digits.match_whole_string("1")

def test_one_digit(one_digit):
    assert one_digit.match_whole_string("1")
    assert not one_digit.match_whole_string("")
    assert not one_digit.match_whole_string("A")

def test_two_digits(two_digits):
    assert two_digits.match_whole_string("12")
    assert not two_digits.match_whole_string("1a")
    assert not two_digits.match_whole_string("1")
    assert not two_digits.match_whole_string("")

def test_less_than_zero_digits_raises_exception():
    with pytest.raises(ReadyRegexException):
        Digits(-1)