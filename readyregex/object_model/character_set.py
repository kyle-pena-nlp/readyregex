from dataclasses import dataclass, field
from typing import Sequence, Union, List
from .character_set_item import CharacterSetItem
from .character import Character
from .pattern import Pattern

@dataclass
class CharacterSet(Pattern):
    
    positives: Union[str,CharacterSetItem,List[Union[CharacterSetItem, str]]] = field(default_factory = list)
    negatives: Union[str,CharacterSetItem,List[Union[CharacterSetItem, str]]] = field(default_factory = list)

    def __post_init__(self):
        self.positives = self._normalize_input(self.positives)
        self.negatives = self._normalize_input(self.negatives)
        self._validate_types()

    def _normalize_input(self, x):
        if isinstance(x, str):
            return [ Character(character) for character in x ]
        elif isinstance(x, CharacterSetItem):
            return [ x ]
        elif isinstance(x, list):
            return [ Character(item) if isinstance(item,str) else item for item in x ]
        


    def include(self, item : Union[CharacterSetItem, str]):
        items = self._normalize_input(item)
        for item in items:
            if item not in self.positives:
                self.positives.append(item)
            if item in self.negatives:
                self.negatives.remove(item)

    def exclude(self, item : Union[CharacterSetItem, str]):
        items = self._normalize_input(item)
        for item in items:
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

