#!/usr/bin/env python

"""Tests for `readyregex` package."""

import pytest

from readyregex import *
from readyregex.common_regex.phone_number import PhoneNumber
from readyregex.object_model.options import Repetitions
from readyregex.object_model.pattern import Pattern

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