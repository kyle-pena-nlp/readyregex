from dataclasses import dataclass, field
from concatenatable import Concatenatable
from typing import Sequence
from pattern import Pattern

@dataclass
class Choice(Concatenatable):

    choices : list[Pattern] = field(default_factory = list)

    def regex(self):
        return "|".join("({})".format(choice.regex()) for choice in self.choices)