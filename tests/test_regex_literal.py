#!/usr/bin/env python

"""Tests for `readyregex` package."""

import pytest

from readyregex import RegexLiteral

@pytest.fixture
def literal_pattern():
    return RegexLiteral("bo?(o|a)")

def test_literal_pattern(literal_pattern):
    assert literal_pattern.match_whole_string("boo")
    assert literal_pattern.match_whole_string("boa")
    assert literal_pattern.match_whole_string("bo")
    assert literal_pattern.match_whole_string("ba")
    assert not literal_pattern.match_whole_string("blam")