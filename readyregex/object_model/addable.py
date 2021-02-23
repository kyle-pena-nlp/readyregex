from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from addable_base import AddableBase
from addable_sequence import AddableSequence


@dataclass
class Addable(AddableBase, ABC):
    
    def add(self, other : AddableBase) -> AddableSequence:
        return AddableSequence(self._get_content_array() + other._get_content_array())

    def __add__(self, other : AddableBase) -> AddableSequence:
        return self.add(other)




