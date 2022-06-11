from dataclasses import dataclass, field
from decimal import Decimal
from enum import Enum, Flag
from ..object_model.pattern import *
from ..object_model.options import *

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