from abc import ABC, ABCMeta
from dataclasses import dataclass
from typing import List, Tuple
import enum

class EnrichedEnumBase(enum.Flag):

    def __new__(cls, *args, **kwds):
        value = 2**(len(cls.__members__))
        obj = object.__new__(cls)
        obj._value_ = value
        return obj

    def __and__(self, other):
        a = self.value
        b = other.value
        c = a & b
        return type(self)(c)

    def __or__(self, other):
        a = self.value
        b = other.value
        c = a | b
        return type(self)(c)

    def __xor__(self, other):
        a = self.value
        b = other.value
        c = a ^ b
        return type(self)(c)

    def __lshift__(self, other):
        a = self.value
        b = other.value
        c = a << b
        return type(self)(c)

    def __rshift__(self, other):
        a = self.value
        b = other.value
        c = a >> b
        return type(self)(c)

    def __invert__(self):
        a = self.value
        return type(self)(~a)