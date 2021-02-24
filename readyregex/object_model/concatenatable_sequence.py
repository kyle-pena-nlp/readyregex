from dataclasses import dataclass, field
from typing import Sequence
from concatenatable_base import ConcatenatableBase

@dataclass
class ConcatenatableSequence(ConcatenatableBase):
    
    concatenatables : list[ConcatenatableBase] = field(default_factory = list)

    def regex(self):
        return "".join(concatenatable.regex() for concatenatable in self.concatenatables)

    def add(self, other : ConcatenatableBase):
        self_content  = self.concatenatables
        other_content = other._get_array_content()
        return ConcatenatableSequence(self_content + other_content)

    def __add__(self, other : ConcatenatableBase):
        return self.add(other)