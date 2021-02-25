from dataclasses import dataclass
from .concatenatable_mixin import ConcatenatableMixin
from .pattern import Pattern

@dataclass
class Digits(Pattern, ConcatenatableMixin):

    number : int

    def __post_init__(self):
        assert self.number >= 0

    def regex(self):
        return r"\d{{{}}}".format(self.number)

