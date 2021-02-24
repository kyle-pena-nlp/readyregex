import re
from dataclasses import dataclass
from concatenatable import Concatenatable
from character_set_item import CharacterSetItem

@dataclass
class Character(Concatenatable, CharacterSetItem):
    
    value : str

    def __post_init__(self, value : str):
        assert len(value) == 1
        self.value = value

    def regex(self):
        return re.escape(self.value)

    def character_set_regex(self):
        if self.value == "]":
            return r"\]"
        elif self.value == "-":
            return r"\-"
        else:
            return re.escape(self.value)