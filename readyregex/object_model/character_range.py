from dataclasses import dataclass
from .character_set_item import CharacterSetItem
from .pattern import Pattern
from .character import Character
from .concatenatable_mixin import ConcatenatableMixin

@dataclass
class CharacterRange(Pattern, ConcatenatableMixin, CharacterSetItem):

    start : str
    end : str

    def __post_init__(self):
        assert len(self.start) == len(self.end) == 1
        assert ord(self.start) <= ord(self.end)

    def regex(self):
        return "[{}]".format(self.character_set_regex())

    def character_set_regex(self):
        return "{}-{}".format(Character(self.start).character_set_regex(), Character(self.end).character_set_regex())