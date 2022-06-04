#!/usr/bin/env python

"""Tests for `readyregex` package."""

import pytest

from readyregex import *
from readyregex.object_model.options import RepetitionOptions

@pytest.fixture
def default_pn():
    return PhoneNumber()

def test_default(default_pn : Pattern):
    assert default_pn.match("904 123 4567")
    assert default_pn.match("(904) 123 4567")
    assert default_pn.match("(904)-123-4567")
    assert default_pn.match("904-123-4567")

@pytest.fixture
def ignore_extra_whitespace():
    return PhoneNumber(Options.IgnoreExtraWhitespace)  


def test_ignore_whitespace(ignore_extra_whitespace : Pattern):
    assert ignore_extra_whitespace.match("904  123 4567")
    assert ignore_extra_whitespace.match("904 123  4567")
    assert ignore_extra_whitespace.match("904 - 123 4567")
    assert ignore_extra_whitespace.match("904 123 - 4567")
    assert ignore_extra_whitespace.match("( 904 ) 123 4567")
    assert ignore_extra_whitespace.match("(904) 123\t4567")


@pytest.fixture  
def mandatory_area_code_parentheses():
    return PhoneNumber(Options.MandatoryAreaCodeParentheses)

def test_mandatory_area_code_parentheses(mandatory_area_code_parentheses : Pattern):
    assert mandatory_area_code_parentheses.match("(904)-123-4567")
    assert not mandatory_area_code_parentheses.match("904-123-4567")

@pytest.fixture  
def no_area_code_parentheses():
    return PhoneNumber(areacode_parentheses=Options.No)

def test_no_area_code_parentheses(no_area_code_parentheses : Pattern):
    assert no_area_code_parentheses.match("904-123-4567")
    assert not no_area_code_parentheses.match("(904)-123-4567")

@pytest.fixture  
def optional_area_code():
    return PhoneNumber(areacode=Options.Optional)

def test_optional_area_code(optional_area_code : Pattern):
    assert optional_area_code.match("123-4567")
    assert optional_area_code.match("904-123-4567")

@pytest.fixture  
def no_area_code():
    return PhoneNumber(areacode=Options.No)

def test_no_area_code(no_area_code : Pattern):
    assert no_area_code.match("123-4567")
    assert not no_area_code.match("904-123-4567")


@pytest.fixture  
def single_dash_separators():
    return PhoneNumber(dashes=Options.Mandatory)

def test_single_dash_separators(single_dash_separators : Pattern):
    assert single_dash_separators.match("904-123-4567")
    assert not single_dash_separators.match("904-123 4567")
    assert not single_dash_separators.match("904-123--4567")

@pytest.fixture  
def single_space_separators():
    return PhoneNumber(dashes = Options.No, extra_whitespace_amount=RepetitionOptions.ExactlyOnce)

def test_only_single_space_separators(single_space_separators : Pattern):
    assert single_space_separators.match("904 123 4567")
    assert not single_space_separators.match("904-123-4567")
    assert not single_space_separators.match("904-123 4567")
    assert not single_space_separators.match("904 123  4567")

@pytest.fixture
def no_separators():
    return PhoneNumber(dashses = Options.No, extra_whitespace=RepetitionOptions.None_)

def test_no_separators(no_separators : Pattern):
    assert no_separators.match("9041234567")
    assert not no_separators.match("904 1234567")
