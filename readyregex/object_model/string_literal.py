import re
from dataclasses import dataclass

from readyregex.object_model.repetition_mixin import RepetitionMixin
from .concatenatable_mixin import ConcatenatableMixin
from .pattern import Pattern

@dataclass
class StringLiteral(Pattern, ConcatenatableMixin, RepetitionMixin):

    regex_escaped_string : str
    
    def __post_init__(self):
        self.regex_escaped_string = re.escape(self.regex_escaped_string)
        self._validate_types()

    def regex(self):
        return self.regex_escaped_string
    
