#!/usr/bin/env python

"""Tests for `readyregex` package."""

import pytest

from readyregex import *

@pytest.fixture
def basic_SSN():
    return SSN()

def test_basic_SSN(basic_SSN):
    assert basic_SSN.match_whole_string("123-45-7890")
    assert not basic_SSN.match_whole_string("1")

@pytest.fixture
def basic_SSN_with_single_space_ignored():
    return SSN(extra_spaces = Repetitions.AtMostOne)

def test_with_single_spaces(basic_SSN_with_single_space_ignored):
    assert basic_SSN_with_single_space_ignored.match_whole_string("123-45-7890")
    assert basic_SSN_with_single_space_ignored.match_whole_string("123- 45-7890")
    assert basic_SSN_with_single_space_ignored.match_whole_string("123 -45-7890")
    assert basic_SSN_with_single_space_ignored.match_whole_string("123-45 -7890")
    assert basic_SSN_with_single_space_ignored.match_whole_string("123-45- 7890")
    assert basic_SSN_with_single_space_ignored.match_whole_string("123-45 - 7890")    
