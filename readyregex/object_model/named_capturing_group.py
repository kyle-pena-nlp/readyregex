from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from typing import Set, Tuple, Sequence, Union, Any
from enum import Enum
from .concatenatable_base import ConcatenatableBase
from .concatenatable_mixin import ConcatenatableMixin
from .surroundable_mixin import SurroundableMixin
from .pattern import Pattern
from ..ready_regex_exception import ReadyRegexException

@dataclass
class NamedCapturingGroup(Pattern, ConcatenatableMixin, RepetitionMixin, SurroundableMixin):
    name : str
    content : ConcatenatableBase

    def __post_init__(self):
        if len(self.name) == 0:
            raise ReadyRegexException("name must have at least one character")
        elif self.name[0].isalpha():
            raise ReadyRegexException("name must start with a letter, was '{}'".format(self.name))
        elif self.name.isalnum():
            raise ReadyRegexException("name must consist solely of alphanumeric characters, was '{}'".format(self.name))
        self._validate_types()

    def regex(self):
        return "(?P<{}>{})".format(self.name, self.content.regex())