#!/usr/bin/env python

"""Tests for `readyregex` package."""

import pytest

from readyregex import *

@pytest.fixture
def A_Z_range_pattern():
    return CharacterRange("A", "Z")

@pytest.fixture
def basic_phone_number():
    return PhoneNumber()

@pytest.fixture
def ignore_whitespace_phone_number():
    return PhoneNumber(Options.IgnoreExtraWhitespace)    

def test_basic_phone_number(basic_phone_number):
    assert basic_phone_number.match("904 123 4567")
    assert basic_phone_number.match("(904) 123 4567")
    assert basic_phone_number.match("(904)-123-4567")
    assert basic_phone_number.match("904-123-4567")

def test_ignore_whitespace_phone_number(ignore_whitespace_phone_number):
    assert ignore_whitespace_phone_number.match("904  123 4567")
    assert ignore_whitespace_phone_number.match("904 123  4567")
    assert ignore_whitespace_phone_number.match("904 - 123 4567")
    assert ignore_whitespace_phone_number.match("904 123 - 4567")
    assert ignore_whitespace_phone_number.match("( 904 ) 123 4567")
    assert ignore_whitespace_phone_number.match("(904) 123\t4567")

