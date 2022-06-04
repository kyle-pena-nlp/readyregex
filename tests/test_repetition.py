#!/usr/bin/env python

"""Tests for `readyregex` package."""

import pytest

from readyregex import *

@pytest.fixture
def kleene_star_init_using_Character():
    return Repetition(Character("a"), None, None)

def test_kleene_star_init_using_Character(kleene_star_init_using_Character):
    assert kleene_star_init_using_Character.match_whole_string("")
    assert kleene_star_init_using_Character.match_whole_string("a")
    assert kleene_star_init_using_Character.match_whole_string("aa")

@pytest.fixture
def kleene_star_init_using_str():
    return Repetition(Character("a"), None, None) 

def test_kleene_star_init_using_character(kleene_star_init_using_str):
    assert kleene_star_init_using_str.match_whole_string("")
    assert kleene_star_init_using_str.match_whole_string("a")
    assert kleene_star_init_using_str.match_whole_string("aa")

@pytest.fixture
def kleene_star_init_using_None_None():
    return Repetition(Character("a"), None, None)

def test_kleene_star_init_using_None_None(kleene_star_init_using_None_None):
    assert kleene_star_init_using_None_None.match_whole_string("")
    assert kleene_star_init_using_None_None.match_whole_string("a")
    assert kleene_star_init_using_None_None.match_whole_string("aa")

@pytest.fixture
def kleene_star_init_using_0_None():
    return Repetition(Character("a"), 0, None)

def test_kleene_star_init_using_0_None(kleene_star_init_using_0_None):
    assert kleene_star_init_using_0_None.match_whole_string("")
    assert kleene_star_init_using_0_None.match_whole_string("a")
    assert kleene_star_init_using_0_None.match_whole_string("aa")

@pytest.fixture
def rep_0_0():
    return Repetition(Character("a"), 0, 0)

def test_rep_0_0(rep_0_0):
    assert rep_0_0.match_whole_string("")
    assert not rep_0_0.match_whole_string("a")
    assert not rep_0_0.match_whole_string("aa")

@pytest.fixture
def rep_1_1():
    return Repetition(Character("a"), 1, 1)

def test_rep_1_1(rep_1_1):
    assert rep_1_1.match_whole_string("a")
    assert not rep_1_1.match_whole_string("")
    assert not rep_1_1.match_whole_string("aa")

@pytest.fixture
def rep_1_2():
    return Repetition(Character("a"), 1, 2)

def test_rep_1_2(rep_1_2):
    assert rep_1_2.match_whole_string("a")
    assert rep_1_2.match_whole_string("aa") 
    assert not rep_1_2.match_whole_string("aaa")
    assert not rep_1_2.match_whole_string("")

@pytest.fixture
def rep_0_1():
    return Repetition(Character("a"), 0, 1)

def test_rep_0_1(rep_0_1):
    assert rep_0_1.match_whole_string("")
    assert rep_0_1.match_whole_string("a")
    assert not rep_0_1.match_whole_string("aa")

@pytest.fixture
def rep_max_1():
    return Repetition(Character("a"), None, 1)

def test_rep_max_1(rep_max_1):
    assert rep_max_1.match_whole_string("")
    assert rep_max_1.match_whole_string("a")
    assert not rep_max_1.match_whole_string("aa")

@pytest.fixture
def rep_max_2():
    return Repetition(Character("a"), None, 2)

def test_rep_max_2(rep_max_2):
    assert rep_max_2.match_whole_string("")
    assert rep_max_2.match_whole_string("a")
    assert rep_max_2.match_whole_string("aa")
    assert not rep_max_2.match_whole_string("aaa")  

@pytest.fixture 
def rep_min_1():
    return Repetition("a", 1, None)

def test_rep_min_1(rep_min_1):
    assert rep_min_1.match_whole_string("a")
    assert rep_min_1.match_whole_string("aa")
    assert not rep_min_1.match_whole_string("")

@pytest.fixture
def rep_min_2():
    return Repetition(Character("a"), 2, None)

def test_rep_min_2(rep_min_2):
    assert rep_min_2.match_whole_string("aa")
    assert rep_min_2.match_whole_string("aaa")
    assert not rep_min_2.match_whole_string("a")
    assert not rep_min_2.match_whole_string("")

def test_reverse_order_bounds_raises_error():
    
    with pytest.raises(ReadyRegexException):
        Repetition(Character("a"), 1, 0)
    
    with pytest.raises(ReadyRegexException):
        Repetition(Character("a"), 2, 1)


def test_negative_bounds_raises_error():

    with pytest.raises(ReadyRegexException):
        Repetition(Character("a"), -1, None)

    with pytest.raises(ReadyRegexException):
        Repetition(Character("a"), None, -1) 

    with pytest.raises(ReadyRegexException):
        Repetition(Character("a"), -2, -1)        

def test_double_kleene_star_does_not_cause_exception():
    Repetition(RegexLiteral("a*"), 0, None)
    Repetition(Repetition(Character("a"), 0, None), 0, None)