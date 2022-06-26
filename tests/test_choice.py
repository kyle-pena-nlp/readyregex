#!/usr/bin/env python

"""Tests for `readyregex` package."""

import pytest

from readyregex import Choice, StringLiteral, Pattern

@pytest.fixture
def simple_choice():
    return Choice([StringLiteral("a"), StringLiteral("b")])

def test_simple_choice(simple_choice : Pattern):
    assert simple_choice.match("a")
    assert simple_choice.match("b")
    assert not simple_choice.match("c")

@pytest.fixture
def string_initialization():
    return Choice([ "a", "b" ])

def test_string_initialization(string_initialization):
    pat = string_initialization
    assert pat.match("a")
    assert pat.match("b")
    assert not pat.match("c")

@pytest.fixture
def empty_choice():
    return Choice([])

def test_empty_choice(empty_choice):
    assert empty_choice.match("")
    assert not empty_choice.match_whole_string("a")

@pytest.fixture
def single_choice():
    return Choice([ "a" ])

def test_single_choice(single_choice):
    assert single_choice.match("a")
    assert not single_choice.match("b")

@pytest.fixture
def multicharacter_choices():
    return Choice(["abc", "def" ])

def test_multicharacter_choices(multicharacter_choices):
    pat = multicharacter_choices
    assert pat.match("abc")
    assert pat.match("def")
    assert not pat.match("c")
    assert not pat.match("d")

