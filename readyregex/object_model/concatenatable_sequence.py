from dataclasses import dataclass, field
from typing import Sequence
from .pattern import Pattern
from .concatenatable_base import ConcatenatableBase

@dataclass
class ConcatenatableSequence(ConcatenatableBase, Pattern):
    
    concatenatables : Sequence[ConcatenatableBase] = field(default_factory = list)

    def _get_content_array(self):
        return self.concatenatables

    def add(self, other : ConcatenatableBase) -> 'ConcatenatableSequence':
        return ConcatenatableSequence(self._get_content_array() + other._get_content_array())

    def __add__(self, other : ConcatenatableBase) -> 'ConcatenatableSequence':
        return self.add(other)

    def regex(self):
        return "".join(concatenatable.regex() for concatenatable in self.concatenatables)