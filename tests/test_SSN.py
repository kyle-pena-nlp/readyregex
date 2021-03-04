#!/usr/bin/env python

"""Tests for `readyregex` package."""

import pytest

from readyregex import *

@pytest.fixture
def basic_SSN():
    return SSN()

def test_basic_SSN(basic_SSN):
    assert basic_SSN.match_whole_string("123456789")
    assert basic_SSN.match_whole_string("123-45-7890")
    assert not basic_SSN.match_whole_string("1")

@pytest.fixture
def basic_SSN_with_whitespace_ignored():
    return SSN(Options.IgnoreExtraWhitespace)

def test_with_spaces(basic_SSN_with_whitespace_ignored):
    assert basic_SSN_with_whitespace_ignored.match_whole_string("123- 45 -  7890")
