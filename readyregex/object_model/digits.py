from dataclasses import dataclass
from .concatenatable_mixin import ConcatenatableMixin
from .pattern import Pattern
from ..ready_regex_exception import ReadyRegexException

@dataclass
class Digits(Pattern, ConcatenatableMixin):

    number : int

    def __post_init__(self):
        if self.number < 0:
            raise ReadyRegexException("number must be greater than or equal to zero, was {}.".format(self.number))

    def regex(self):
        return r"\d{{{}}}".format(self.number)

