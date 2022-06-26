from dataclasses import dataclass
from enum import Flag
from typing import Optional
from ..object_model.pattern import Pattern

class PasswordRequirements(Flag):
    SpecialCharacter = 1
    Number = 2
    Letter = 4
    Uppercase = 8
    Lowercase = 16

@dataclass
class Password(Pattern):
    requirements : PasswordRequirements
    minimum_length: int
    maximum_length: Optional[int]