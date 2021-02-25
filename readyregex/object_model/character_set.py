from dataclasses import dataclass, field
from typing import Sequence, Union
from .concatenatable_mixin import ConcatenatableMixin
from .character_set_item import CharacterSetItem
from .character import Character

@dataclass
class CharacterSet(ConcatenatableMixin):
    
    positives: Sequence[Union[CharacterSetItem, str]] = field(default_factory = list)
    negatives: Sequence[Union[CharacterSetItem, str]] = field(default_factory = list)

    def __post_init__(self):
        self.positives = [ Character(item) if isinstance(item,str) else item for item in self.positives ]
        self.negatives = [ Character(item) if isinstance(item,str) else item for item in self.negatives ]

    def regex(self):
        
        positives_regex = "".join( positive.character_set_regex() for positive in self.positives )
        negatives_regex = "".join( negative.character_set_regex() for negative in self.negatives )

        if negatives_regex:
            return "[{}^{}]".format(positives_regex, negatives_regex)
        else:
            return "[{}]".format(positives_regex)

