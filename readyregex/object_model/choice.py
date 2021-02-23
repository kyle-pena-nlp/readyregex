from dataclasses import dataclass, field
from addable import Addable
from typing import Sequence
from pattern import Pattern

@dataclass
class Choice(Addable):

    choices : Sequence[Pattern] = field(default_factory = list)

    def regex(self):
        return "|".join("({})".format(choice.regex()) for choice in self.choices)