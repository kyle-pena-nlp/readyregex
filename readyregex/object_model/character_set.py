from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from typing import Set, Tuple, Sequence, Union, Any
from enum import Enum
from pattern import Pattern
from character_set_item import CharacterSetItem

@dataclass
class CharacterSet(Pattern):
    
    positives: Sequence[CharacterSetItem] = field(default_factory = list)
    negatives: Sequence[CharacterSetItem] = field(default_factory = list)

    def regex(self):
        
        positives_regex = "".join( positive.regex() for positive in self.positives )
        negatives_regex = "".join( negative.regex() for negative in self.negatives )

        if negatives_regex:
            return "[{}^{}]".format(positives_regex, negatives_regex)
        else:
            return "[{}]".format(positives_regex)

    def add(self, other : CharacterSetItem) -> 'CharacterSet':
        return CharacterSet(positives = list(self.positives) + [other], negatives = list(self.negatives))

    def __add__(self, other : CharacterSetItem) -> 'CharacterSet':
        return self.add(other)

    def subtract(self, other : CharacterSetItem) -> 'CharacterSet':
        return CharacterSet(positives = list(self.positives), negatives = list(self.negatives) + [other])

    def __sub__(self, other : CharacterSetItem) -> 'CharacterSet':
        return self.subtract(other)

