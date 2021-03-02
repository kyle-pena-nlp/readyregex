#!/usr/bin/env python

"""Tests for `readyregex` package."""

import pytest

from readyregex import *

@pytest.fixture
def A():
    return Character("A")

def test_A(A):
    return A.match_whole_string("A")

@pytest.fixture
def unicode_character():
    return Character("Æ")

def test_unicode_character(unicode_character):
    unicode_character.match_whole_string("Æ")

def test_fails_not_single_character():
    with pytest.raises(ReadyRegexException):
        _ = Character("")
    with pytest.raises(ReadyRegexException):
        _ = Character("ab")