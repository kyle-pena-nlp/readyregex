from dataclasses import dataclass, field
from typing import Sequence, Union

from readyregex.object_model.repetition_mixin import RepetitionMixin
from .pattern import Pattern
from .concatenatable_base import ConcatenatableBase

@dataclass
class ConcatenatableSequence(Pattern, ConcatenatableBase, RepetitionMixin):
    
    concatenatables : Sequence[ConcatenatableBase] = field(default_factory = list)

    def _get_content_array(self):
        return self.concatenatables

    def add(self, other : ConcatenatableBase) -> ConcatenatableBase:
        return ConcatenatableSequence(self._get_content_array() + other._get_content_array())

    def __add__(self, other : ConcatenatableBase) -> ConcatenatableBase:
        return self.add(other)

    def join(self, others : Sequence[ConcatenatableBase]) -> ConcatenatableBase:
        parts = []
        for i, part in enumerate(others):
            parts.append(part)
            if i < len(others) - 1:
                parts.append(self)
        return ConcatenatableSequence(parts)        

    def regex(self):
        return "".join(concatenatable.regex() for concatenatable in self.concatenatables)