#!/usr/bin/env python

"""Tests for `readyregex` package."""

import pytest

from readyregex import *

@pytest.fixture
def A_Z_range_pattern():
    return Range("A", "Z")

@pytest.fixture
def basic_latin_character_range_pattern():
    return Range(chr(0X0000), chr(0x007F))

@pytest.fixture
def latin_1_supplement_character_range_pattern():
    return Range(chr(0X0000), chr(0x00FF))

def test_A_Z_range_pattern(A_Z_range_pattern):
    assert A_Z_range_pattern.match("A")
    assert A_Z_range_pattern.match("Z")
    assert not A_Z_range_pattern.match("0")

def test_basic_latin_character_range_pattern(basic_latin_character_range_pattern):
    assert basic_latin_character_range_pattern.match("a")
    assert basic_latin_character_range_pattern.match("Z")
    assert basic_latin_character_range_pattern.match("9")
    assert basic_latin_character_range_pattern.match("{")

def test_latin_1_supplement_character_range_pattern(latin_1_supplement_character_range_pattern):
    assert latin_1_supplement_character_range_pattern.match("a")
    assert latin_1_supplement_character_range_pattern.match("Z")
    assert latin_1_supplement_character_range_pattern.match("9")
    assert latin_1_supplement_character_range_pattern.match("{")
    assert latin_1_supplement_character_range_pattern.match("é")

def test_non_character_input_raises_exception():
    with pytest.raises(ReadyRegexException):
        Range("ab", "c")
    with pytest.raises(ReadyRegexException):
        Range("a", "bc")     

def test_character_range_must_be_in_order():
    with pytest.raises(ReadyRegexException):
        Range("z", "a")  
