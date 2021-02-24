from dataclasses import dataclass
from character_set_item import CharacterSetItem
from character import Character
from concatenatable import Concatenatable

@dataclass
class CharacterRange(Concatenatable, CharacterSetItem):

    start : str
    end : str

    def __post_init__(self, start : str, end : str):
        assert len(start) == len(end) == 1
        assert ord(start) <= ord(end)
        self.start = start
        self.end = end

    def regex(self):
        return "[{}]".format(self.character_set_regex())

    def character_set_regex(self):
        return "{}-{}".format(Character(self.start).character_set_regex(), Character(self.end).character_set_regex())