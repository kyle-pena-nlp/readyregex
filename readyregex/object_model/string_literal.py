import re
from dataclasses import dataclass
from .concatenatable_mixin import ConcatenatableMixin

@dataclass
class StringLiteral(ConcatenatableMixin):

    regex_escaped_string : str
    
    def __post_init__(self):
        self.regex_escaped_string = re.escape(self.string)

    def regex(self):
        return self.regex_escaped_string
    
