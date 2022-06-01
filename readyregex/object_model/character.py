import re
from dataclasses import dataclass
from .concatenatable_mixin import ConcatenatableMixin
from .character_set_item import CharacterSetItem
from .pattern import Pattern
from ..ready_regex_exception import ReadyRegexException

@dataclass
class Character(Pattern, ConcatenatableMixin, RepetitionMixin, CharacterSetItem):
    
    value : str

    def __post_init__(self):
        if len(self.value) != 1:
            raise ReadyRegexException("Not a character: '{}'".format(self.value))
        self._validate_types()

    def regex(self):
        return re.escape(self.value)

    def character_set_regex(self):
        if self.value == "]":
            return r"\]"
        elif self.value == "-":
            return r"\-"
        else:
            return re.escape(self.value)