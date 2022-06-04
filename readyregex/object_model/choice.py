from dataclasses import dataclass, field
from typing import Sequence

from readyregex.object_model.repetition_mixin import RepetitionMixin
from .pattern import Pattern
from .concatenatable_mixin import ConcatenatableMixin
from .string_literal import StringLiteral

@dataclass
class Choice(Pattern, ConcatenatableMixin, RepetitionMixin):

    choices : Sequence[Pattern] = field(default_factory = list)

    def __post_init__(self):
        self.choices = [ StringLiteral(item) if isinstance(item,str) else item for item in self.choices ]
        self._validate_types()

    def regex(self):
        return "({})".format("|".join("({})".format(choice.regex()) for choice in self.choices))

    def or_(self, other: Pattern):
        return Choice(self.choices + other)

    def __or__(self, other : Pattern):
        return self.or_(other)