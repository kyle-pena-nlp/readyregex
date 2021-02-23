from dataclasses import dataclass
from addable import Addable

@dataclass
class Digits(Addable):

    number : int

    def __post_init__(self, number):
        assert number >= 0
        self.number = number

    def regex(self):
        return r"\d{{{}}}".format(self.number)

