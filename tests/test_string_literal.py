#!/usr/bin/env python

"""Tests for `readyregex` package."""

import pytest

from readyregex import *

@pytest.fixture
def empty_string_literal():
    return StringLiteral("")

def test_empty_string_literal(empty_string_literal):
    assert empty_string_literal.match_whole_string("")
    assert not empty_string_literal.match_whole_string("a")
    assert not empty_string_literal.match_whole_string(" ")

@pytest.fixture
def string_literal_that_looks_like_regex():
    return StringLiteral(r"\d{3}-[a-zA-Z]")

def test_string_literal_that_looks_like_regex(string_literal_that_looks_like_regex):
    assert string_literal_that_looks_like_regex.match_whole_string(r"\d{3}-[a-zA-Z]")