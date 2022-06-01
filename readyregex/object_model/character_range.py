from dataclasses import dataclass
from .character_set_item import CharacterSetItem
from .pattern import Pattern
from .character import Character
from .concatenatable_mixin import ConcatenatableMixin
from ..ready_regex_exception import ReadyRegexException

@dataclass
class CharacterRange(Pattern, ConcatenatableMixin, RepetitionMixin, CharacterSetItem):

    start : str
    end : str

    def __post_init__(self):
        if len(self.start) != 1 or len(self.end) != 1:
            raise ReadyRegexException("start and end must both be single characters, was: '{}' and '{}'".format(self.start, self.end))
        if ord(self.start) > ord(self.end):
            raise ReadyRegexException("start character must be less than end character, was '{}' ({}) and '{}' ({})".format(self.start, ord(self.start), self.end, ord(self.end)))
        self._validate_types()

    def regex(self):
        return "[{}]".format(self.character_set_regex())

    def character_set_regex(self):
        return "{}-{}".format(Character(self.start).character_set_regex(), Character(self.end).character_set_regex())