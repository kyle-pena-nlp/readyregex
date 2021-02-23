from dataclasses import dataclass, field
from typing import Sequence
from addable_base import AddableBase

@dataclass
class AddableSequence(AddableBase):
    
    addables : Sequence[AddableBase] = field(default_factory = list)

    def regex(self):
        return "".join(addable.regex() for addable in self.addables)

    def add(self, other : AddableBase):
        self_content  = self.addables
        other_content = other._get_array_content()
        return AddableSequence(self_content + other_content)

    def __add__(self, other : AddableBase):
        return self.add(other)