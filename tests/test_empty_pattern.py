#!/usr/bin/env python

"""Tests for `readyregex` package."""

import pytest

from readyregex import *

@pytest.fixture
def empty_pattern():
    return EmptyPattern()

def test_empty_pattern(empty_pattern):
    assert empty_pattern.match_whole_string("")
    assert not empty_pattern.match_whole_string(" ")