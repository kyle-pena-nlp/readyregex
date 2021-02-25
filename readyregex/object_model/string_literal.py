import re
from dataclasses import dataclass
from .concatenatable_mixin import ConcatenatableMixin
from .pattern import Pattern

@dataclass
class StringLiteral(Pattern, ConcatenatableMixin):

    regex_escaped_string : str
    
    def __post_init__(self):
        self.regex_escaped_string = re.escape(self.regex_escaped_string)

    def regex(self):
        return self.regex_escaped_string
    
