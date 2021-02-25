from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from typing import Union
from .pattern import Pattern
from .concatenatable_sequence import ConcatenatableSequence
from .concatenatable_base import ConcatenatableBase

@dataclass
class ConcatenatableMixin(ConcatenatableBase, ABC):

    def _get_content_array(self):
        return [ self ]
    
    def add(self, other : ConcatenatableBase) -> ConcatenatableSequence:
        return ConcatenatableSequence(self._get_content_array() + other._get_content_array())

    def __add__(self, other : ConcatenatableBase) -> ConcatenatableSequence:
        return self.add(other)





