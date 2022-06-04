import re
from dataclasses import dataclass
from .pattern import Pattern

@dataclass
class StringLiteral(Pattern):

    regex_escaped_string : str
    
    def __post_init__(self):
        self.regex_escaped_string = re.escape(self.regex_escaped_string)
        self._validate_types()

    def regex(self):
        return self.regex_escaped_string
    
