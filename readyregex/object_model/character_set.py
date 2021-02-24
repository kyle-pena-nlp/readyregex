from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from typing import Set, Tuple, Sequence, Union, Any
from enum import Enum
from concatenatable import Concatenatable
from character_set_item import CharacterSetItem
from character import Character

@dataclass
class CharacterSet(Concatenatable):
    
    positives: list[Union[CharacterSetItem, str]] = field(default_factory = list)
    negatives: list[Union[CharacterSetItem, str]] = field(default_factory = list)

    def __post_init__(self, positives, negatives):
        self.positives = [ Character(item) if isinstance(item,str) else item for item in positives ]
        self.negatives = [ Character(item) if isinstance(item,str) else item for item in negatives ]

    def regex(self):
        
        positives_regex = "".join( positive.character_set_regex() for positive in self.positives )
        negatives_regex = "".join( negative.character_set_regex() for negative in self.negatives )

        if negatives_regex:
            return "[{}^{}]".format(positives_regex, negatives_regex)
        else:
            return "[{}]".format(positives_regex)

