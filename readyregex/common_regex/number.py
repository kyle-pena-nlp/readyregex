from dataclasses import dataclass
from enum import Enum
from ..object_model.pattern import Pattern
from ..object_model.options import Options

class NumberType(Enum):
    Any = 0
    Whole = 1
    Decimal = 2
    Scientific = 4
    eNotation = 8

@dataclass
class Number(Pattern):

    number_type : NumberType
    negative_sign : Options

    def build(self):

        # Options: Whole, Decimal, Scientific, Negative, etc., combinations, per the readme suggestions.  Not sure about fraction?  Maybe this is a separate pattern.

        raise Exception("Unimplemented.")