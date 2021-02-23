from dataclasses import dataclass
from enum import Enum

@dataclass
class SpecialCharacterClassInfo:
    value : int
    regex : str

_S = SpecialCharacterClassInfo

class SpecialCharacterClasses(Enum):

    ALL                         = _S(1, r".")
    DIGITS                      = _S(2, r"\d")
    NON_DIGITS                  = _S(3, r"\D")
    WHITESPACE                  = _S(4, r"\s")
    NON_WHITESPACE              = _S(5, r"\S")
    ALPHANUMERIC_UNDERSCORE     = _S(6, r"\w")
    NON_ALPHANUMERIC_UNDERSCORE = _S(7, r"\W")
    WORD_BOUNDARY               = _S(8, r"\b")
    NON_WORD_BOUNDARY           = _S(9, r"\B")
    STRING_BEGIN                = _S(10, r"\A")
    STRING_END                  = _S(11, r"\Z")
    LINE_BEGIN                  = _S(12, r"^")
    LINE_END                    = _S(12, r"$")

    # todo: unicode character classes, etc.


