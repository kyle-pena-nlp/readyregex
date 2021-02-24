from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from concatenatable_base import ConcatenatableBase
from concatenatable_sequence import ConcatenatableSequence


@dataclass
class Concatenatable(ConcatenatableBase, ABC):
    
    def add(self, other : ConcatenatableBase) -> ConcatenatableSequence:
        return ConcatenatableSequence(self._get_content_array() + other._get_content_array())

    def __add__(self, other : ConcatenatableBase) -> ConcatenatableSequence:
        return self.add(other)




