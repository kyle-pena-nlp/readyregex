#!/usr/bin/env python

"""Tests for `readyregex` package."""

import pytest

from readyregex import *

@pytest.fixture
def default_pn():
    return PhoneNumber()



"""
    MandatoryAreaCodeParentheses = enum.auto()
    NoAreaCodeParentheses = enum.auto()
    OptionalAreaCode    = enum.auto()
    NoAreaCode          = enum.auto()
    OnlyDashSeparators  = enum.auto()
    OnlySpaceSeparators = enum.auto()    
    NoSeparators        = enum.auto()
    OptionalSeparators  = enum.auto() 
"""

def test_default(default_pn):
    assert default_pn.match("904 123 4567")
    assert default_pn.match("(904) 123 4567")
    assert default_pn.match("(904)-123-4567")
    assert default_pn.match("904-123-4567")

@pytest.fixture
def ignore_extra_whitespace():
    return PhoneNumber(Options.IgnoreExtraWhitespace)  


def test_ignore_whitespace(ignore_extra_whitespace):
    assert ignore_extra_whitespace.match("904  123 4567")
    assert ignore_extra_whitespace.match("904 123  4567")
    assert ignore_extra_whitespace.match("904 - 123 4567")
    assert ignore_extra_whitespace.match("904 123 - 4567")
    assert ignore_extra_whitespace.match("( 904 ) 123 4567")
    assert ignore_extra_whitespace.match("(904) 123\t4567")


@pytest.fixture  
def mandatory_area_code_parentheses():
    return PhoneNumber(Options.MandatoryAreaCodeParentheses)

def test_mandatory_area_code_parentheses(mandatory_area_code_parentheses):
    assert mandatory_area_code_parentheses.match("(904)-123-4567")
    assert not mandatory_area_code_parentheses.match("904-123-4567")

@pytest.fixture  
def no_area_code_parentheses():
    return PhoneNumber(Options.NoAreaCodeParentheses)

def test_no_area_code_parentheses(no_area_code_parentheses):
    assert no_area_code_parentheses.match("904-123-4567")
    assert not no_area_code_parentheses.match("(904)-123-4567")

@pytest.fixture  
def optional_area_code():
    return PhoneNumber(Options.OptionalAreaCode)

def test_optional_area_code(optional_area_code):
    assert optional_area_code.match("123-4567")
    assert optional_area_code.match("904-123-4567")

@pytest.fixture  
def no_area_code():
    return PhoneNumber(Options.NoAreaCode)

def test_no_area_code(no_area_code):
    assert no_area_code.match("123-4567")
    assert not no_area_code.match("904-123-4567")


@pytest.fixture  
def single_dash_separators():
    return PhoneNumber(Options.SingleDashSeparators)

def test_single_dash_separators(single_dash_separators):
    assert single_dash_separators.match("904-123-4567")
    assert not single_dash_separators.match("904-123 4567")
    assert not single_dash_separators.match("904-123--4567")

@pytest.fixture  
def single_space_separators():
    return PhoneNumber(Options.SingleSpaceSeparators)

def test_only_single_space_separators(single_space_separators):
    assert single_space_separators.match("904 123 4567")
    assert not single_space_separators.match("904-123-4567")
    assert not single_space_separators.match("904-123 4567")
    assert not single_space_separators.match("904 123  4567")

@pytest.fixture
def no_separators():
    return PhoneNumber(Options.NoSeparators)

def test_no_separators(no_separators):
    assert no_separators.match("9041234567")
    assert not no_separators.match("904 1234567")
