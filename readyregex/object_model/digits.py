from dataclasses import dataclass
from .concatenatable_mixin import ConcatenatableMixin

@dataclass
class Digits(ConcatenatableMixin):

    number : int

    def __post_init__(self):
        assert self.number >= 0

    def regex(self):
        return r"\d{{{}}}".format(self.number)

