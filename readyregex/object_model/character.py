import re
from dataclasses import dataclass
from .concatenatable_mixin import ConcatenatableMixin
from .character_set_item import CharacterSetItem

@dataclass
class Character(ConcatenatableMixin, CharacterSetItem):
    
    value : str

    def __post_init__(self):
        assert len(self.value) == 1

    def regex(self):
        return re.escape(self.value)

    def character_set_regex(self):
        if self.value == "]":
            return r"\]"
        elif self.value == "-":
            return r"\-"
        else:
            return re.escape(self.value)