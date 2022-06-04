from dataclasses import dataclass, field
from typing import Sequence

from .pattern import Pattern

@dataclass
class Choice(Pattern):

    choices : Sequence[Pattern] = field(default_factory = list)

    def __post_init__(self):
        self.choices = [ StringLiteral(item) if isinstance(item,str) else item for item in self.choices ]
        self._validate_types()

    def regex(self):
        return "({})".format("|".join("({})".format(choice.regex()) for choice in self.choices))