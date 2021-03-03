#!/usr/bin/env python

"""Tests for `readyregex` package."""

import pytest

from readyregex import *

@pytest.fixture
def optional_empty():
    return Optional(EmptyPattern())

@pytest.fixture
def optional_character():
    return Optional(Character("a"))

def test_optional_empty(optional_empty):
    assert optional_empty.match_whole_string("")

def test_optional_character(optional_character):
    assert optional_character.match_whole_string("")
    assert optional_character.match_whole_string("a")
    assert not optional_character.match_whole_string("b")