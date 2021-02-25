from dataclasses import dataclass, field
from typing import Sequence
from pattern import Pattern
from .concatenatable_mixin import ConcatenatableMixin

@dataclass
class Choice(ConcatenatableMixin):

    choices : Sequence[Pattern] = field(default_factory = list)

    def regex(self):
        return "|".join("({})".format(choice.regex()) for choice in self.choices)