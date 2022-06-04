#!/usr/bin/env python

"""Tests for `readyregex` package."""

import pytest

from readyregex import *

@pytest.fixture
def A():
    return CharacterSet(positives = [ Character("A") ])

def test_just_A(A):
    assert A.match_whole_string("A")
    assert not A.match_whole_string("B")

@pytest.fixture
def A_str():
    return CharacterSet(positives = [ "A" ])

def test_A_str(A_str):
    assert A_str.match_whole_string("A")
    assert not A_str.match_whole_string("B") 

@pytest.fixture
def A_Z():
    return CharacterSet(positives = [ Range("A", "Z") ])

def test_A_Z(A_Z):
    assert A_Z.match("A")
    assert A_Z.match("B")
    assert not A_Z.match("0")

@pytest.fixture
def A_Z_and_0_9():
    return CharacterSet(positives = [ Range("A", "Z"), Range("0", "9") ])

def test_A_Z_and_0_9(A_Z_and_0_9):
    assert A_Z_and_0_9.match("A")
    assert A_Z_and_0_9.match("C")
    assert A_Z_and_0_9.match("Z")
    assert A_Z_and_0_9.match("0")
    assert A_Z_and_0_9.match("9")
    assert not A_Z_and_0_9.match(".")

@pytest.fixture
def not_0_9():
    return CharacterSet(positives = [ ], negatives = [ Range("0", "9") ])

def test_not_0_9(not_0_9):
    assert not_0_9.match("A")
    assert not not_0_9.match("0")

@pytest.fixture
def special_character_class():
    return CharacterSet(positives = [ SpecialCharacterClasses.DIGITS ])

def test_special_class(special_character_class):
    assert special_character_class.match("0")
    assert not special_character_class.match("A")

