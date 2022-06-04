from dataclasses import dataclass, field
from typing import Sequence, Union, List

from readyregex.object_model.repetition_mixin import RepetitionMixin
from .concatenatable_mixin import ConcatenatableMixin
from .character_set_item import CharacterSetItem
from .character import Character
from .pattern import Pattern

@dataclass
class CharacterSet(Pattern, ConcatenatableMixin, RepetitionMixin):
    
    positives: List[Union[CharacterSetItem, str]] = field(default_factory = list)
    negatives: List[Union[CharacterSetItem, str]] = field(default_factory = list)

    def __post_init__(self):
        self.positives = [ Character(item) if isinstance(item,str) else item for item in self.positives ]
        self.negatives = [ Character(item) if isinstance(item,str) else item for item in self.negatives ]
        self._validate_types()

    def include(self, item : Union[CharacterSetItem, str]):
        if item not in self.positives:
            self.positives.append(item)
        if item in self.negatives:
            self.negatives.remove(item)

    def exclude(self, item : Union[CharacterSetItem, str]):
        if item in self.positives:
            self.positives.remove(item)
        if item not in self.negatives:
            self.negatives.append(item)

    def regex(self):
        
        # TODO: character set specific escape patterns for characters
        positives_regex = "".join( positive.character_set_regex() for positive in self.positives )
        negatives_regex = "".join( negative.character_set_regex() for negative in self.negatives )

        if negatives_regex:
            return "[{}^{}]".format(positives_regex, negatives_regex)
        else:
            return "[{}]".format(positives_regex)

