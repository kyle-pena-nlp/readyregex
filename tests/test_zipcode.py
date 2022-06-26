#!/usr/bin/env python

"""Tests for `readyregex` package."""

import pytest

from readyregex import Zipcode

@pytest.fixture
def default_zipcode():
    return Zipcode()