#!/usr/bin/env python

"""Tests for `readyregex` package."""

import pytest

from readyregex import Pattern, PhoneNumber

@pytest.fixture
def default_pn():
    return PhoneNumber()

def test_default(default_pn : Pattern):
    assert default_pn.match("904 123 4567")
    assert default_pn.match("(904) 123 4567")
    assert default_pn.match("(904)-123-4567")
    assert default_pn.match("904-123-4567")
    assert default_pn.match("904 - 123 - 4567")
    assert default_pn.match("904 123-4567")
    assert default_pn.match("(904) 123-4567")